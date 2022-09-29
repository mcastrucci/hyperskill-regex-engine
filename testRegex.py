import unittest
import regex as rx


class TestRegex(unittest.TestCase):

    def test_string_content_is_equal(self):
        """This test attempts to test when a string contains the regex string"""
        regex = "apple"
        strings_to_test = ['apple', 'this apple tastes good', 'applex', 'applementics']

        for string in strings_to_test:
            self.assertEqual(rx.test_string_with_regex(regex, string), True, f'Expected True with regex {regex} and string {string}')

    def test_dot_wildcard(self):
        """This test tests the function of the dot wildcard It should be True for any value where the wildcard is located"""
        self.assertEqual(rx.test_string_with_regex(".", 'apple'), True, f'Expected true with regex . and string apple')
        self.assertEqual(rx.test_string_with_regex("a.ple", 'acple'), True, f'Expected true with regex a.ple and string acple')
        self.assertEqual(rx.test_string_with_regex("a.ple", 'atcple'), False, f'Expected false with regex a.ple and string aacple')
        self.assertEqual(rx.test_string_with_regex("a.p..", 'ahpac'), True, f'Expected false with regex a.p.. and string ahpac')

    def test_begining_wildcard(self):
        """This test attempts to test the ^ wildcard, it means that the match should be at the begning of the string"""
        self.assertEqual(rx.test_string_with_regex('^app', 'apple'), True, f'Expected True with regex ^app and string apple')
        self.assertEqual(rx.test_string_with_regex('^app', 'capple'), False, f'Expected False with regex ^app and string capple')
        self.assertEqual(rx.test_string_with_regex('^rapid', 'rapidify'), True, f'Expected True with regex ^rapid and string rapidify')
        self.assertEqual(rx.test_string_with_regex('^rapid', 'caprapid'), False, f'Expected False with regex ^rapid and string caprapid')

    def test_ending_wildcard(self):
        """This test attempts to test the $ wildcard, it means that the match should be at the end of the string"""
        self.assertEqual(rx.test_string_with_regex('app$', 'apple'), False, f'Expected False with regex app$ and string apple')
        self.assertEqual(rx.test_string_with_regex('ple$', 'capple'), True, f'Expected True with regex ple$ and string capple')
        self.assertEqual(rx.test_string_with_regex('rapid$', 'rapidify'), False, f'Expected False with regex rapid$ and string rapidify')
        self.assertEqual(rx.test_string_with_regex('rapid$', 'caprapid'), True, f'Expected True with regex rapid$ and string caprapid')

    def hyperskill_test_cases(self):
        """This test attempts The test cases from hyperskill"""
        test_cases = [
            ("^app", "apple", True),
            ("le$", "apple", True),
            ("^a", "apple", True),
            (".$", "apple", True),
            ("apple$", "tasty apple", True),
            ("^apple", "apple pie", True),
            ("apple$", "apple", True),
            ("^apple$", "tasty apple", False),
            ("^apple$", "apple pie", False),
            ("app$", "apple", False),
            ("^le", "apple", False)
        ]

        for test_case in test_cases:
            self.assertEqual(rx.test_string_with_regex(test_case[0], test_case[1]), test_case[2])


if __name__ == '__main__':
    unittest.main()
