import unittest

from main import process_words, clear_text


class TestClearText(unittest.TestCase):

    def test_simple_text(self):
        given = "Hello world Hello Python"
        expected = ["hello", "world", "hello", "python"]

        result = clear_text(given)
        self.assertEqual(result, expected)


class TestProcessWords(unittest.TestCase):
    def test_empty_text(self):
        text = []
        expected_words = {}
        expected_top_t = [("", 0), ("", 0), ("", 0)]
        result_words, result_top_t = process_words(text)
        self.assertDictEqual(result_words, expected_words)
        self.assertListEqual(result_top_t, expected_top_t)

    def test_single_word(self):
        text = ["hello"]
        expected_words = {"hello": 1}
        expected_top_t = [("hello", 1), ("", 0), ("", 0)]
        result_words, result_top_t = process_words(text)
        self.assertDictEqual(result_words, expected_words)
        self.assertListEqual(result_top_t, expected_top_t)

    def test_multiple_words(self):
        text = ["hello", "world", "hello", "test"]
        expected_words = {"hello": 2, "world": 1, "test": 1}
        expected_top_t = [("hello", 2), ("world", 1), ("test", 1)]
        result_words, result_top_t = process_words(text)
        self.assertDictEqual(result_words, expected_words)
        self.assertListEqual(result_top_t, expected_top_t)

    def test_more_than_three_unique_words(self):
        text = ["a", "b", "c", "d", "a", "b", "a"]
        expected_words = {"a": 3, "b": 2, "c": 1, "d": 1}
        expected_top_t = [("a", 3), ("b", 2), ("c", 1)]
        result_words, result_top_t = process_words(text)
        self.assertDictEqual(result_words, expected_words)
        self.assertListEqual(result_top_t, expected_top_t)
