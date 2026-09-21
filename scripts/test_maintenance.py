"""Regression checks for maintenance failures that previously passed silently."""
import contextlib
import io
import ssl
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import check_links
import check_markdown
import refresh_counts
import refresh_repository_status
import sync_audit


class LinkChecks(unittest.TestCase):
    def test_vendor_and_lookalike_urls_are_checked(self):
        for url in ('https://openai.com/missing', 'https://example.com/openai.com',
                    'https://shields.io.evil.example/path'):
            self.assertFalse(check_links.should_skip(url))
        self.assertTrue(check_links.should_skip('https://img.shields.io/badge/test'))
        self.assertEqual(check_links.SSL_CTX.verify_mode, ssl.CERT_REQUIRED)

    def test_head_404_requires_get_confirmation(self):
        with patch.object(check_links, 'request', side_effect=[(404, 'https://example.com'), (200, 'https://example.com')]) as request:
            self.assertEqual(check_links.check_url('https://example.com')['status'], 'OK')
            self.assertEqual([call.args[1] for call in request.call_args_list], ['HEAD', 'GET'])

    def test_dead_blocked_and_transient_are_distinct(self):
        for code, expected in ((404, 'DEAD'), (410, 'DEAD'), (403, 'BLOCKED'), (429, 'BLOCKED'), (503, 'ERROR')):
            with self.subTest(code=code), patch.object(check_links, 'request', return_value=(code, 'https://example.com')):
                self.assertEqual(check_links.check_url('https://example.com', retries=0)['status'], expected)

    def test_strict_mode_fails_unresolved(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'README.md').write_text('- [Example](https://example.com)\n')
            result = {'url': 'https://example.com', 'status': 'BLOCKED', 'code': 403, 'final_url': 'https://example.com'}
            with patch.object(check_links, 'ROOT', root), patch.object(check_links, 'check_url', return_value=result), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(check_links.main(['--files', 'README.md', '--strict']), 1)


class CatalogueChecks(unittest.TestCase):
    def test_nonexistent_duplicate_heading_anchor_is_not_accepted(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'README.md'
            path.write_text('# Heading\n[Broken](#heading-5)\n', encoding='utf-8')
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(check_markdown.check(path), 1)

    def test_counts_exclude_toc_and_fences_and_keep_emoji_anchor(self):
        lines = ['## Contents', '- [Frameworks](#️-frameworks)', '## 🏗️ Frameworks',
                 '- [Real](https://example.com)', '```markdown', '- [Sample](https://example.org)', '```']
        counts = refresh_counts.section_counts(lines)
        self.assertEqual(sum(counts.values()), 1)
        self.assertEqual(counts['️-frameworks'], 1)

    def test_advisory_rows_are_not_resources(self):
        lines = ['## 🗺️ Guide', '### Examples', '**First case**', '→ advice', '**Second case**',
                 '## ⚠️ Anti-Picks', '| Avoid | Use |', '|---|---|', '| A | B |']
        counts = refresh_counts.advisory_counts(lines)
        self.assertEqual(counts[refresh_counts.slugify('## 🗺️ Guide')], 2)
        self.assertEqual(counts[refresh_counts.slugify('## ⚠️ Anti-Picks')], 1)
        self.assertEqual(sum(refresh_counts.section_counts(lines).values()), 0)

    def test_missing_translated_table_row_fails_even_with_equal_entries(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            english = '## Catalogue\n- [A](https://example.com)\n| Tool | Docs |\n|---|---|\n| A | [Docs](https://example.com/docs) |\n'
            files = {lang: root/f'{lang}.md' for lang in ('en', 'zh', 'ja')}
            for lang, path in files.items():
                path.write_text(english if lang != 'ja' else english.rsplit('| A |', 1)[0], encoding='utf-8')
            with patch.object(sync_audit, 'FILES', files), patch('sys.argv', ['sync_audit.py']), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(sync_audit.main(), 1)

    def test_archival_annotation_is_idempotent_and_entry_scoped(self):
        original = '- [Tool](https://github.com/org/tool) - Description.\n- [Other](https://example.com) - See https://github.com/org/tool.\n'
        once, changed = refresh_repository_status.mark_archived(original, {'org/tool'})
        self.assertEqual(changed, ['org/tool'])
        self.assertEqual(once.count('📦'), 1)
        self.assertEqual(refresh_repository_status.mark_archived(once, {'org/tool'}), (once, []))

    def test_repository_scan_excludes_github_product_routes(self):
        text = '- [Copilot](https://github.com/features/copilot) - Product.\n- [Tool](https://github.com/org/tool) - Repository.\n'
        self.assertEqual(refresh_repository_status.listed_repos(text), {'org/tool'})


if __name__ == '__main__':
    unittest.main()
