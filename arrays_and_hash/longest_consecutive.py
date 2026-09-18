def longest_consecutive(nums):
    num_set = set(nums)
    result = 0
    for n in num_set:
        if n - 1 not in num_set:
            curr = n
            count = 0
            while curr in num_set:
                curr += 1
                count += 1
            result = max(count, result)
    return result


# Time O(n)

if __name__ == '__main__':
    nums = [2, 20, 4, 10, 3, 4, 5, 12, 13, 14, 15, 16, 17, 18, 19, 1, 20, 0, 21, 22]
    print(longest_consecutive(nums))  # expected: 11 (12 through 22)

    nums = [3, 2, 5, 4, 6, 1, 1, 0]
    print(longest_consecutive(nums))  # expected: 7 (0 through 6)

    nums = []
    print(longest_consecutive(nums))  # expected: 0
