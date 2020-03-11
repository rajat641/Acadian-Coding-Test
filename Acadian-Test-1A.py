"""
Problem Statement -Write a function that takes in a string S, a character C1, and another character C2, and
switches occurrences of C1 in the first half of string S with occurrences of C2 in the second half of string S.
 The function should only switch these characters until one of the sides runs out of their respective character.
The switching should be done from the outsides of the strings inward; in other words, it should always replace
outermost characters first.

Algorithm-
Step 1: Take 2 pointers one at the starting index of string and other at the end index of string.
Step 2:  Check if the starting index points at swapping character 1 and ending index points at swapping character 2
        - If yes, then swap the characters and increment/decrement the respective pointers.
        - If no,increment/decrement the respective pointers.
Step 3: Always check if the pointers are within limits
Step 4: Return the final string after converting a list to a string.

"""


def swap_string(s, rep_first_char_1, rep_second_char_1):
    s_length = len(s)
    """
    Base Case: When length of string is less than 2, we return the input string
    """
    if s_length < 2:
        return s
    # converting a string to a list as its immutable
    s = list(s)
    if s_length == 2:
        if s[0] == rep_first_char_1 and s[1] == rep_second_char_1:
            s[0], s[1] = s[1], s[0]
        return ''.join(s)
    left_end = 0
    right_end = s_length-1
    left_limit = int(s_length/2 - 1)
    right_limit = int(s_length/2)

    while left_end <= left_limit and right_end >= right_limit:
        if s[left_end] == rep_first_char_1 and s[right_end] == rep_second_char_1:
            s[left_end], s[right_end] = s[right_end], s[left_end]
            left_end = left_end + 1
            right_end = right_end - 1
        elif s[left_end] == rep_first_char_1:
            right_end = right_end - 1
        elif s[right_end] == rep_second_char_1:
            left_end = left_end + 1
        else:
            left_end = left_end + 1
            right_end = right_end - 1
    return ''.join(s)


if __name__ == '__main__':
    # taking input from user namely a test string, swapping characters
    test_string = input()
    rep_first_char = input()
    rep_second_char = input()
    print(swap_string(test_string, rep_first_char, rep_second_char))
