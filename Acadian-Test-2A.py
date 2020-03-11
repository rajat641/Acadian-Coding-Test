"""
Problem Statement -Write a function that takes in a string S, a character C1, and another character C2, and
switches occurrences of C1 in the first half of string S with occurrences of C2 in the second half of string S.
 The function should only switch these characters until one of the sides runs out of their respective character.
The switching should be done from the outsides of the strings inward; in other words, it should always replace
outermost characters first.

Assumption -
If the string is odd length, we take the middle character to be the first character of the second half

Algorithm-
Step 1: Take 2 pointers one at the starting index of string and other at the end index of string.
Step 2:  Check if the starting index points at swapping string 1 and ending index points at swapping string 2
        - If yes, then swap the strings and increment/decrement the respective pointers.
        - If no,increment/decrement the respective pointers.
Step 3: Always check if the pointers are within limits
Step 4: Return the final string after converting a list to a string.

"""


def check_equal(s, pointer, limit, rep_string):
    for i, v in enumerate(rep_string):
        if pointer + i >= limit or rep_string[i] != s[pointer + i]:
            return False
    return True


def set_null_end(s, i):
    s[i] = '\0'


def swap_string(s, rep_first_string_1, rep_second_string_1):
    s_length, rep_first_string_length, rep_second_string_length = len(s),\
                                                                  len(rep_first_string_1), len(rep_second_string_1)
    if s_length < rep_first_string_length + rep_second_string_length \
            or len(rep_first_string_1) == 0 or len(rep_second_string_1) == 0:
        return s
    s, a, b = list(s), list(rep_first_string_1), list(rep_second_string_1)

    i, j, count = 0, s_length - 1, 0
    right_limit = s_length >> 1
    while i < right_limit <= j:
        if check_equal(s, i, right_limit, rep_first_string_1):
            while j >= right_limit:
                if check_equal(s, j, s_length, rep_second_string_1):
                    [set_null_end(s, i+k) for k in range(rep_first_string_length)]
                    [set_null_end(s, j+k) for k in range(rep_second_string_length)]
                    count += 2
                    j -= 1
                    break
                j -= 1
            i += rep_first_string_length-1
        i += 1

    ns = []
    i, c = 0, count >> 1
    while i < s_length:
        if s[i] == '\0':
            if i < (s_length >> 1) and count >= c:
                i += rep_first_string_length-1
                ns += rep_second_string_1
            else:
                i += rep_second_string_length-1
                ns += rep_first_string_1
            count -= 1
        else:
            ns.append(s[i])
        i += 1
    return ''.join(ns)


if __name__ == '__main__':
    test_string = input()
    rep_first_string = input()
    rep_second_string = input()
    print(swap_string(test_string, rep_first_string, rep_second_string))