def middle_number(s1, s2):
    a, b = sorted((s1, s2), key=len)
    len_a, len_b = len(a), len(b)
    len_half = int((len_a + len_b - 1) / 2)
    lo, hi = 0, len_a - 1
    while lo < hi:
        i = int((lo + hi) / 2)
        j = len_half - i - 1
        if a[i] >= b[j]:
            hi = i
        else:
            lo = i + 1
    second_middle_offset = (len_a + len_b + 1) % 2
    i = lo
    j = len_half - i - 1
    if (i == (len_a - 1) and j >= 0 and a[i] < b[j]) or (i == 0 and a[i] > b[j + 1]):
        result = b[j: j + 2]
    else:
        result = sorted(a[i:i + 2] + b[len_half - i: len_half - i + 2])
    print(result)
    return (result[0] + result[second_middle_offset]) / 2


def generate_sequence(mask, size):
    s1 = []
    s2 = []
    for index in range(size):
        if mask & (0x1 << index):
            s1.append(index)
        else:
            s2.append(index)
    return s1, s2


def test(size):
    for mask in range(1, (0x1 << size) - 1):
        s1, s2 = generate_sequence(mask, size)
        expected = (size - 1) / 2
        actual = middle_number(s1, s2)
        if expected != actual:
            print(s1)
            print(s2)
            print("Expected:%.1f, Actual:%.1f" % (expected, actual))
            return


test(10)
# print("Expected:2, Actual:", middle_number([2], [1,3]))  #2
# print("Expected:2.5, Actual:", middle_number([1,2], [3,4]))  #2, 3
# print("Expected:16, Actual:", middle_number([1,12,15,26,38], [2,13,17,30,45]))  #15, 17
# print("Expected:17, Actual:", middle_number([1,12,15,26,38], [2,13,17,30,45,50])) #17
# print("Expected:10.5, Actual:", middle_number([1,2,5,6,8], [13,17,30,45,50]))  #8, 13
# print("Expected:9.5, Actual:", middle_number([1,2,5,6,8,9,10], [13,17,30,45,50]))  #9, 10
