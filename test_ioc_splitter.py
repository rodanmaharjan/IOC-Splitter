import unittest
from ioc_splitter import IOCSplitter

class TestIOCSplitterInit(unittest.TestCase):
    def setUp(self):
        self.input_file_path = 'input.txt'
        self.ip_output_path = 'ip.txt'
        self.domain_output_path = 'domain.txt'
        self.url_output_path = 'url.txt'
        self.hash_output_path = 'hash.txt'
        self.final_output_path = 'final.txt'
        
        self.splitter = IOCSplitter(
            input_file_path=self.input_file_path,
            ip_output_path=self.ip_output_path,
            domain_output_path=self.domain_output_path,
            url_output_path=self.url_output_path,
            hash_output_path=self.hash_output_path,
            final_output_path=self.final_output_path
        )

    def test_initialization(self):
        self.assertEqual(self.splitter.input_file_path, self.input_file_path)
        self.assertEqual(self.splitter.ip_output_path, self.ip_output_path)
        self.assertEqual(self.splitter.domain_output_path, self.domain_output_path)
        self.assertEqual(self.splitter.url_output_path, self.url_output_path)
        self.assertEqual(self.splitter.hash_output_path, self.hash_output_path)
        self.assertEqual(self.splitter.final_output_path, self.final_output_path)

        self.assertEqual(self.splitter.ip_values, [])
        self.assertEqual(self.splitter.domain_values, [])
        self.assertEqual(self.splitter.url_values, [])
        self.assertEqual(self.splitter.hash_values, [])

        self.assertIsNotNone(self.splitter.url_pattern)
        self.assertIsNotNone(self.splitter.ip_pattern)
        self.assertIsNotNone(self.splitter.hash_pattern)
        self.assertIsNotNone(self.splitter.domain_pattern)

    def test_regex_patterns(self):
        self.assertTrue(self.splitter.url_pattern.match('http://example.com'))
        self.assertTrue(self.splitter.url_pattern.match('https://example.com'))
        self.assertTrue(self.splitter.ip_pattern.match('192.168.1.1'))
        self.assertTrue(self.splitter.hash_pattern.match('d41d8cd98f00b204e9800998ecf8427e'))
        self.assertTrue(self.splitter.domain_pattern.match('example.com'))
        self.assertFalse(self.splitter.url_pattern.match('example.com'))
        self.assertFalse(self.splitter.ip_pattern.match('example.com'))
        self.assertFalse(self.splitter.hash_pattern.match('example.com'))
        self.assertFalse(self.splitter.domain_pattern.match('something'))

if __name__ == '__main__':
    unittest.main()