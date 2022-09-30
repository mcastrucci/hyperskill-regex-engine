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
        self.assertEqual(rx.test_string_with_regex('le$', 'apple'), True, f'Expected True with regex rapid$ and string caprapid')
        self.assertEqual(rx.test_string_with_regex('.$', 'apple'), True, f'Expected True with regex rapid$ and string caprapid')
        self.assertEqual(rx.test_string_with_regex('apple$', 'tasty apple'), True, f'Expected True with regex rapid$ and string caprapid')
        self.assertEqual(rx.test_string_with_regex('app$', 'apple'), False, f'Expected True with regex rapid$ and string caprapid')


    def test_hyperskill_test_cases(self):
        """This test attempts The test cases from hyperskill"""
        test_cases = [
        ("a", "a",          "True",     "Two identical patterns should return True!"),
        ("a", "b",          "False",    "Two different patterns should not return True!"),
        ("7", "7",          "True",     "Two identical patterns should return True!"),
        ("6", "7",          "False",    "Two different patterns should not return True!"),
        (".", "a",          "True",     "Don't forget that '.' is a wild-card that matches any single character."),
        ("a", ".",          "False",    "A period in the input string is still a literal!"),
        ("", "a",           "True",     "An empty regex always returns True!"),
        ("", "",            "True",     "An empty regex always returns True!"),
        ("a", "",           "False",    "A non-empty regex and an empty input string always returns False!"),
        # stage 2
        ("apple", "apple",  "True",     "Two identical equal-length patterns should return True!"),
        (".pple", "apple",  "True",     "The wild-card '.' should match any single character in a string."),
        ("appl.", "apple",  "True",     "The wild-card '.' should match any single character in a string."),
        (".....", "apple",  "True",     "The wild-card '.' should match any single character in a string."),
        ("", "apple",       "True",     "An empty regex always returns True!"),
        ("apple", "",       "False",    "A non-empty regex and an empty input string always returns False!"),
        ("apple", "peach",  "False",    "Two different patterns should not return True!"),
        # stage 3
        ("le", "apple",     "True",     "If the input string contains the regex, it should return True!"),
        ("app", "apple",    "True",     "If the input string contains the regex, it should return True!"),
        ("a", "apple",      "True",     "If the input string contains the regex, it should return True!"),
        (".", "apple",      "True",     "Even a single wild-card character '.' can produce a match!"),
        ("apwle", "apple",  "False",    "Two different patterns should not return True!"),
        ("peach", "apple",  "False",    "Two different patterns should not return True!"),
        # stage 4
        ('^app', 'apple',           "True",
            "A regex starting with '^' should match the following pattern only at the beginning of the input string!"),
        ('le$', 'apple',            "True",
            "A regex ending with '$' should match the preceding pattern only at the end of the input string!"),
        ('^a', 'apple',             "True",
            "A regex starting with '^' should match the following pattern only at the beginning of the input string!"),
        ('.$', 'apple',             "True",
            "A regex ending with '$' should match the preceding pattern only at the end of the input string!"),
        ('apple$', 'tasty apple',   "True",
            "A regex ending with '$' should match the preceding pattern only at the end of the input string!"),
        ('^apple', 'apple pie',     "True",
            "A regex starting with '^' should match the following pattern only at the beginning of the input string!"),
        ('^apple$', 'apple',        "True",
            "A regex starting with '^' and ending with '$' should match only the enclosed literals!"),
        ('^apple$', 'tasty apple',  "False",
            "A regex starting with '^' and ending with '$' should match only the enclosed literals!"),
        ('^apple$', 'apple pie',    "False",
            "A regex starting with '^' and ending with '$' should match only the enclosed literals!"),
        ('app$', 'apple',           "False",
            "A regex ending with '$' should match the preceding pattern only at the end of the input string!"),
        ('^le', 'apple',            "False",
            "A regex starting with '^' should match the following pattern only at the beginning of the input string!"),
        # stage 5
        ("colou?r", "color",        "True",
            "'?' in a regex should match the preceding character exactly 0 or 1 times!"),
        ("colou?r", "colour",       "True",
            "'?' in a regex should match the preceding character exactly 0 or 1 times!"),
        ("colou?r", "colouur",      "False",
            "'?' in a regex should match the preceding character exactly 0 or 1 times!"),
        ("colou*r", "color",        "True",
            "'*' in a regex should match the preceding character 0 or more times!"),
        ("colou*r", "colour",       "True",
            "'*' in a regex should match the preceding character 0 or more times!"),
        ("colou*r", "colouur",      "True",
            "'*' in a regex should match the preceding character 0 or more times!"),
        ("colou+r", "colour",        "True",
             "'+' in a regex should match the preceding character 1 or more times!"),
        ("colou+r", "color",        "False",
            "'+' in a regex should match the preceding character 1 or more times!"),
        (".*", "aaa",               "True",
            "The repetition operators can be combined with the wild card '.'!"),
        (".+", "aaa",               "True",
            "The repetition operators can be combined with the wild card '.'!"),
        (".?", "aaa",               "True",
            "The repetition operators can be combined with the wild card '.'!"),
        ("no+$", "noooooooope",     "False",
            "The repetition operators can be combined with other metacharacters, like '.', '^' and '$'."),
        ("^no+", "noooooooope",     "True",
            "The repetition operators can be combined with other metacharacters, like '.', '^' and '$'."),
        ("^no+pe$", "noooooooope",     "True",
            "The repetition operators can be combined with other metacharacters, like '.', '^' and '$'."),
        ("^n.+pe$", "noooooooope",     "True",
            "The repetition operators can be combined with other metacharacters, like '.', '^' and '$'."),
        ("^n.+p$", "noooooooope",     "False",
            "The repetition operators can be combined with other metacharacters, like '.', '^' and '$'."),
        ('^.*c$', 'abcabc', "True",
         "The repetition operators can be combined with other metacharacters, like '.', '^' and '$'.")
        ]

        for i in range(len(test_cases)):
            test_case = test_cases[i]
            print("testing", i + 1, "of", len(test_cases), "\n",test_cases[i])
            self.assertEqual(str(rx.test_string_with_regex(test_case[0], test_case[1])), test_case[2], test_case[3])


if __name__ == '__main__':
    unittest.main()
