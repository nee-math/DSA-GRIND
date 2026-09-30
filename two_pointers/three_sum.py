def three_sum(nums):
    """
    Given an integer array `nums`, return all triplets [nums[i], nums[j], nums[k]]
    where i != j, i != k, j != k, and nums[i] + nums[j] + nums[k] == 0.

    The solution set must not contain duplicate triplets. The order of the
    output and the order of the triplets does not matter.
    """

    nums.sort()
    result = []
    for index in range(len(nums)):
        num = nums[index]
        if index != 0 and num == nums[index - 1]:
            continue
        left, right = index + 1, len(nums) - 1
        target = 0 - num
        while left < right:
            r_num = nums[right]
            l_num = nums[left]

            sum = r_num + l_num
            if sum == target:
                result.append([nums[index], nums[right], nums[left]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif sum > target:
                right -= 1
            else:
                left += 1
    return result


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(three_sum(nums))  # expected: [[-1, -1, 2], [-1, 0, 1]]

    nums = [0, 1, 1]
    print(three_sum(nums))  # expected: []

    nums = [0, 0, 0]
    print(three_sum(nums))  # expected: [[0, 0, 0]]

    nums = [0, 0, 0, 0]
    print(three_sum(nums))  # expected: [[0, 0, 0]]

    nums = [-2, 0, 1, 1, 2]
    print(three_sum(nums))  # expected: [[-2, 0, 2], [-2, 1, 1]]

    nums = [1, 2, -2, -1]
    print(three_sum(nums))  # expected: []
