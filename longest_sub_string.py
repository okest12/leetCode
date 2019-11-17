def length_of_longest_substring(s):
    start = 0
    max_len = 0
    max_start = 0
    c_index = {}
    for i, c in enumerate(s):
        if c in c_index:
            start = max(start, c_index[c] + 1)
        c_index[c] = i
        if i - start + 1 >= max_len:
            max_len = i - start + 1
            max_start = start
    return s[max_start:max_start+max_len]


print(length_of_longest_substring("aefbacbcedec"))
