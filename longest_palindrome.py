def longest_palindrome(s):
    result = ''
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_str = s[i:j + 1]
            if is_palindrom(sub_str) and len(sub_str) > len(result):
                result = sub_str
    return result


def is_palindrom(s):
    if s == s[::-1]:
        return True
    return False


def find_palindrome(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]


def longest_palindrome_optimize(s):
    result = ''
    for i in range(len(s)-1):
        if 2 * (len(s) - i) - 1 <= len(result):break
        temp_s = find_palindrome(s, i - 1, i + 1)
        if len(temp_s) > len(result): result = temp_s
        temp_s = find_palindrome(s, i, i + 1)
        if len(temp_s) > len(result): result = temp_s
    return result


print(longest_palindrome("abcbab"))
print(longest_palindrome("aaaa"))
print(longest_palindrome("aaaacc"))
print(longest_palindrome("abvd"))

print(longest_palindrome_optimize("abcbab"))
print(longest_palindrome_optimize("aaaa"))
print(longest_palindrome_optimize("aaaacc"))
print(longest_palindrome_optimize("abcd"))
