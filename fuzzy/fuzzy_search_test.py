from exception_test import FoundedException


def swap(a, b):
    a, b = b, a


def levenshtein_distance(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)

    if str1_len > str2_len:
        swap(str1_len, str2_len)

    distances = range(str1_len + 1)

    for i2, c2 in enumerate(str2):
        distances_ = [i2 + 1]
        for i1, c1 in enumerate(str1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(
                    1 + min((distances[i1], distances[i1 + 1], distances_[-1]))
                )
        distances = distances_

    return distances[-1]


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
                    raise FoundedException()
            return False
        except FoundedException:
            pass

    return True
