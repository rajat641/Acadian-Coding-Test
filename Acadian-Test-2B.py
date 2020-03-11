def check_equal(s, pointer, limit, rep_string):
    for i, v in enumerate(rep_string):
        if pointer + i >= limit or rep_string[i] != s[pointer + i]:
            return False
    return True


def swap_string_recursive(s, a, b):
    def __swap_string_recursive(s, a, b, left_pointer, right_pointer, iend, ma, mb):
        s_length, rep_first_string_length, rep_second_string_length = len(s), len(a), len(b)
        if left_pointer >= iend or right_pointer < (s_length >> 1):
            return list(s)
        ni, nj = left_pointer, right_pointer
        s, a, b = list(s), list(a), list(b)

        ma = ma or check_equal(s, left_pointer, iend, a)
        mb = mb or check_equal(s, right_pointer, s_length, b)
        if not ma and not mb:
            ni += 1
            nj -= 1
        elif ma and not mb:
            nj -= 1
        elif not ma and mb:
            ni += 1
        elif ma and mb:
            s = s[:left_pointer] + b + s[left_pointer+rep_first_string_length:right_pointer] + a + \
                s[right_pointer+rep_second_string_length:s_length]
            iend += rep_second_string_length - rep_first_string_length
            ni += rep_second_string_length
            ma = mb = False
        return __swap_string_recursive(s, a, b, ni, nj, iend, ma, mb)

    s_length, rep_first_string_length, rep_second_string_length = len(s), len(a), len(b)
    return s if (s_length < rep_first_string_length + rep_second_string_length or rep_first_string_length == 0
                 or rep_second_string_length == 0) else \
        ''.join(__swap_string_recursive(s, a, b, 0, s_length - 1, s_length >> 1, False, False))


if __name__ == '__main__':
    test_string = input()
    rep_first_string = input()
    rep_second_string = input()
    print(swap_string_recursive(test_string, rep_first_string, rep_second_string))