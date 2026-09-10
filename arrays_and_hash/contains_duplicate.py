def contains_duplicate(nums):
    return len(set(nums)) != len(nums)

# Complexity
# Space: O(N)
# Time: O(N)

if __name__ == '__main__':
    print(contains_duplicate(nums=[1, 2, 3, 3]))
