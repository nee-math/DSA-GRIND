def contains_duplicate(nums):
    return len(set(nums)) == len(nums)


# Complexity
# Space: O(1)
# Time: O(N)


# Set ->
if __name__ == '__main__':
    input = [[1, 2, 3, 3]]
    for inp in input:
        print(contains_duplicate(nums=inp))
