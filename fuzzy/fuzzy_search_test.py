from exception_test import ErrorException


def fuzzy_search(needle, haystack):
    needle_len = len(needle)
    haystack_len = len(haystack)

    if needle_len > haystack_len:
        return False

    if needle_len == haystack_len:
        return needle_len == haystack_len

    j = -1
    for nch in needle:
        try:
            while j < haystack_len - 1:
                j += 1
                if haystack[j] == nch:
                    raise ErrorException()
            return False
        except ErrorException:
            pass

    return True
