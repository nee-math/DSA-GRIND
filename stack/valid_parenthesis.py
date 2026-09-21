def is_valid(s):
    parenthesis_ref_data = {")": "(", "]": "[", "}": "{"}
    stack = []  # LIFO
    if len(s) % 2 != 0:
        return False
    for i in s:
        if i in parenthesis_ref_data:
            if stack[-1] != parenthesis_ref_data[i]:
                return False
            stack.pop()
        else:
            stack.append(i)
    if len(stack) > 0:
        return False
    return True

# Space O(n)
# Time O(n)

if __name__ == '__main__':
    s = "()[]{}"
    print(is_valid(s))  # expected: True

    s = "(]"
    print(is_valid(s))  # expected: False

    s = "([{}])"
    print(is_valid(s))  # expected: True

    s = "("
    print(is_valid(s))  # expected: False
