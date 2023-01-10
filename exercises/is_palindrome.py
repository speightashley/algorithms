def is_palindrome(s):
    s = s.lower()
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


print(is_palindrome("Abba"))
