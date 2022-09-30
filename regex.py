META_CHARS = ['?', '*', '+', '$', '^']

def main():
    regex, string_to_test = get_user_inputs()

    if len(regex) == 0:
        # If regex len is 0, the operation will be always True
        print_result(True)
    else:
        # Standard case String should be equal or longer
        # than the regex to be able to slice the String
        print_result(test_string_with_regex(regex, string_to_test))


def print_result(result):
    """Prints the result of the regex operation  """
    print(result)


def test_char(char, string_to_test, index, wildcard=False) -> tuple[int, bool]:
    """ tests if the char matches the given string from the given index and returns the
    index where it does not match anymore

    Returns
        the index where the String does not match the char
    """

    if wildcard and wildcard != '$':
        # char is optional or one time
        if wildcard == '?':
            if char == string_to_test[index] or char == '.':
                return (index + 1), True
            else:
                return index, True
        # matches zero or more times
        elif wildcard == '*':
            if char == string_to_test[index] or char == '.':
                # count the next chars if there is more
                next_index = consume_char_n_times(char, string_to_test, index)
                return next_index, True
            else:
                return index, True
        # matches at least one time and n times
        elif wildcard == '+':
            if char == string_to_test[index] or char == '.':
                next_index = consume_char_n_times(char, string_to_test, index)
                return next_index, True
            else:
                return index, False
        else:
            # invalid case
            return index, True
    else:
        # if no wildcard, the char should match the string at the index
        if char == string_to_test[index] or char == '.':
            return (index + 1), True
        else:
            return index, False


def consume_char_n_times(char, string_to_consume, pointer=0, stop_at=None):
    """Consumes a char n times in a string from an pointer

    Returns
        The index that points the next index that is different from the given char
    """
    # count the next chars if there is more
    next_index = pointer
    next_string_char = char
    while next_string_char == char or char == '.' and next_string_char != stop_at:
        try:
            temp_index = next_index + 1
            temp = string_to_consume[temp_index]
        except IndexError:
            return next_index
        else:
            next_index = temp_index
            next_string_char = temp
    return next_index


def test_string_with_regex(regex, string_to_test):
    """Test the string with the given regex if the string could not be matched
    the same function is re-called with a splice of the original string

    Params:
        - regex - The regex to use to test the string
        - string_to_test - The string to test with the regex

    Returns
        - True if there is a match of the string with the Regex
        - False if there is no matches
    """

    # pointer to point the current index of the string to test
    string_pointer = 0
    match_at_start = False
    # Iterate over regex and check string match
    valid = True
    for i in range(len(regex)):
        # check if current index in regex is a meta-char
        if regex[i] in META_CHARS:

            # if the regex char is ^ it will be valid in two situations
            # 1. The string pointer is still at 0
            # 2. The previous char is \n
            if regex[i] == '^':
                if string_pointer == 0:
                    match_at_start = True
                    continue
                elif string_pointer > 0 and string_to_test[string_pointer - 1] == '\n':
                    # if string pointer is higher than 0, it is only valid if the previous char
                    # is a new line
                    match_at_start = False
                    continue
                else:
                    # Invalid string, fails regex
                    valid = False
                    break
            # if regex char is $ means that it should be at the end of a line
            # or end of string, next char should be \n or end of length
            elif regex[i] == '$':
                # string consumed only do not mistake with len -1
                if len(string_to_test) == string_pointer:
                    # valid case, end of the string
                    # if valid and end of regex, the string matches
                    if len(regex) - 1 == i and valid:
                        break
                elif len(string_to_test) - 1 >= string_pointer:
                    if string_to_test[string_pointer] == '\n':
                        string_pointer += 1
                        # This case is only valid if next char is an end of line
                        pass
                    else:
                        # invalid case, not end of line # keep slicing the string
                        valid = test_string_with_regex(regex, string_to_test[1:])
                        break
            elif regex[i] == '?' or regex[i] == '*' or regex[i] == '+':
                # if any of the wildcards is the next regex char, skip it
                continue
        else:
            regex_char = regex[i]
            # check if there is a wildcard after the current char
            wildcard = False
            try:
                next_char = regex[i + 1]
            except IndexError:
                pass  # no next char, end of string
            else:
                if next_char in META_CHARS:
                    wildcard = next_char

            if len(string_to_test) - 1 < string_pointer:
                return False  # no string to test

            char = string_to_test[string_pointer]

            if valid and regex_char == '.' and (wildcard == '+') or (wildcard == '*'):
                # consume everything until next non-metacharacter
                try:
                    temp = regex[i + 2]
                except IndexError:
                    pass
                else:
                    next_regex_char_after_wildcard = temp
                    string_pointer = consume_char_n_times(regex_char, string_to_test, string_pointer, stop_at=next_regex_char_after_wildcard)
                    continue

            if match_at_start and string_pointer == 0:
                if char == regex[i] or regex[i] == '.':
                    # valid case, regex matches
                    string_pointer += 1
                    continue
                else:
                    # first char does not match regex
                    valid = False
                    break
            elif match_at_start and valid:
                index, valid = test_char(regex_char, string_to_test, string_pointer, wildcard)
                string_pointer = index
                if not valid:
                    # since the match should happen at the start, if there is no match
                    # the regex test fails
                    return False
            else:
                index, valid = test_char(regex_char, string_to_test, string_pointer, wildcard)
                string_pointer = index
                # if not valid, make a slice of the string and re-try
                if not valid:
                    valid = test_string_with_regex(regex, string_to_test[1:])
                    break

    return valid


def get_user_inputs():
    """gets the user input for the execution

    Returns:
        - a tuple that represents the regex that the user
        does want to use and the string to test with the regex
    """
    # the input from user should be in this format "regex|string"
    input_from_user = input()
    if '|' in input_from_user:
        return input_from_user.split('|')
    else:
        panic()


def panic():
    print("Error, invalid input")
    exit(0)


if __name__ == '__main__':
    main()
