def is_palindrome(s):
    cleaned_s = ""
    for char in s:
        if char.isalnum():
            if char.isalpha():
                cleaned_s += char.lower()
            else:
                cleaned_s += char
    L, R = 0, len(cleaned_s) - 1

    while L <= R:
        if cleaned_s[L] != cleaned_s[R]:
            return False
        L += 1
        R -= 1
    return True


def is_palindrome_optimal(s):
    L, R = 0, len(s) - 1
    while L <= R:
        left_char = s[L]
        right_char = s[R]
        if not left_char.isalnum():
            L += 1
            continue
        if not right_char.isalnum():
            R -= 1
            continue
        if left_char.lower() != right_char.lower():
            return False
        L += 1
        R -= 1
    return True


# Time complexiy O(N)
# Space complexity O(1)

if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    print(is_palindrome(s))  # expected: True

    s = "race a car"
    print(is_palindrome(s))  # expected: False

    s = " "
    print(is_palindrome(s))  # expected: True

    s = "0P"
    print(is_palindrome(s))  # expected: False

    s = "Was it a car or a cat I saw?"
    print(is_palindrome(s))  # expected: True
