import math
from collections import Counter


def top_k(nums, k):
    nums_freq = Counter(nums)
    top_n = nums_freq.most_common(k)

    return [item[0] for item in top_n]


def get_highest_value(s):
    ans = ()
    max_count = 0

    for k, v in s.items():
        if v > max_count:
            ans = (k, v)
            max_count = v
    return ans


# Space O(n * m)
# Time O(n)

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(top_k(nums, k))  # expected: [1, 2]
