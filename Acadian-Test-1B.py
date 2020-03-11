def swap_string_recursive(s, rep_first_char_1, rep_second_char_1):
    def __swap_string_recursive(s, rep_first_char_1, rep_second_char_1, left_pointer, right_pointer):
        if left_pointer >= (len(s) >> 1) or right_pointer < (len(s) >> 1):
            return s
        ni, nj = left_pointer + 1, right_pointer - 1
        if s[left_pointer] == rep_first_char_1 and s[right_pointer] != rep_second_char_1:
            ni -= 1
        elif s[left_pointer] != rep_first_char_1 and s[right_pointer] == rep_second_char_1:
            nj += 1
        elif s[left_pointer] == rep_first_char_1 and s[right_pointer] == rep_second_char_1:
            s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
        return __swap_string_recursive(s, rep_first_char_1, rep_second_char_1, ni, nj)

    s_length = len(s)
    return s if (s_length < 2 or len(rep_first_char_1) != 1 or len(rep_second_char_1) != 1) \
        else ''.join(__swap_string_recursive(list(s), rep_first_char_1, rep_second_char_1, 0, s_length-1))


if __name__ == '__main__':
    test_string = input()
    rep_first_string = input()
    rep_second_string = input()
    print(swap_string_recursive(test_string, rep_first_string, rep_second_string))
