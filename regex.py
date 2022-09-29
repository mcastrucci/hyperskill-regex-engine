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


def test_string_with_regex(regex, string_to_test):
    """Test the string with the given regex
    If the string is longer than the regex, the function will be called again
    with a slice of the original string until the string is consumed or a match with the
    regex happens.
    It first loop and slice the string from left to right and if there is no match, it loops
    from right to left


    Params:
        - regex - The regex to use to test the string
        - string_to_test - The string to test with the regex

    Returns
        - True if there is a match of the string with the Regex
        - False if there is no matches
    """
    start_wildcard_available = '^' in regex
    end_wildcard_available = '$' in regex
    regex_clean = "".join(regex) # make a copy

    # Check that wildcard appears only one time
    if start_wildcard_available:
        # this is lazzy, probably i should check for scape chars too
        if regex.count('^') > 1:
            return False # invalid regex
        regex_clean = regex_clean.replace("^", "")

    # Check that wildcard appears only one time
    if end_wildcard_available:
        # this is lazzy, probably i should check for scape chars too
        if regex.count('$') > 1:
            return False  # invalid regex
        regex_clean = regex_clean.replace("$", "")

    # If the length of the regex and the string to test are equal
    # the string is tested without further process
    if len(regex_clean) == len(string_to_test):
        # since the string has the same length (without the wildcards)
        # it will be true if it is at the end or at the begining
        return test_string_slice_with_regex(regex_clean, string_to_test)
    elif len(regex_clean) < len(string_to_test):
        # Iterate over the slices of the string to try to match the regex.
        if start_wildcard_available:
            # if regex contains start string wilcard, first slice should match regex, if not
            # we dont continue
            result = test_string_slice_with_regex(regex_clean, string_to_test[:len(regex_clean)])
            if not result:
                return False
            # if there is no other anchors / wildcards, this is a match
            if not end_wildcard_available:
                return True

        if end_wildcard_available:
            # if regex contaisn end wildcard, an slice from the end of the string
            # should match the regex, if not there is not need to process further
            result = test_string_slice_with_regex(regex_clean, string_to_test[-len(regex_clean):])
            if not result:
                return False
            else:
                return True  # this is good enough to return a match

        # If nothing was returned until this point, multiple slices should be done
        # to the string to find matches

        left_to_right_slice = "".join(string_to_test)  # clone of the string
        while len(left_to_right_slice) > len(regex):
            result = test_string_with_regex(regex, left_to_right_slice[0:len(regex)])
            if result is True:
                return True
            else:
                left_to_right_slice = left_to_right_slice[len(regex):]
        # If nothing was returned yet, try from right to left
        right_to_left_slice = "".join(string_to_test)  # clone of the string
        while len(right_to_left_slice) > len(regex):
            result = test_string_with_regex(regex, right_to_left_slice[-len(regex):])
            if result is True:
                return True
            else:
                right_to_left_slice = right_to_left_slice[-1:-len(regex)]
        return False  # nothing was returned before this step
    else:
        # this case means that the string is already consumed and a match is not
        # possible anymore
        return False


def test_string_slice_with_regex(regex, sliced_string):
    """Tests a string slice with a regex (already filtered from starting and ending wildcards)

    Returns
        - True if the string slice matches the regex
        - False otherwise
    """
    if len(regex) == len(sliced_string):
        result = True
        for index in range(len(regex)):
            # If all the regex members matches the string members (or regex value is .)
            # the string matches the regex
            if regex[index] != '.' and sliced_string[index] != regex[index]:
                result = False
        return result
    else:
        # regex and slice do not have the same length
        # this is a bug and should not happen
        return False


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
