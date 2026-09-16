def product_except_self(nums):
    size = len(nums)
    l_nums = []
    l_cummulative = 1
    r_cummulative = 1
    r_nums = [0] * size
    for index in range(size):
        jndex = size - index - 1
        r_nums[jndex] = r_cummulative
        l_nums.append(l_cummulative)
        l_cummulative *= nums[index]
        r_cummulative *= nums[jndex]

    result = []
    for l, r in zip(l_nums, r_nums):
        result.append(l * r)

    return result


if __name__ == '__main__':
    nums = [1, 2, 4, 6]
    print(product_except_self(nums))  # expected: [48, 24, 12, 8]

    nums = [-1, 0, 1, 2, 3]
    print(product_except_self(nums))  # expected: [0, -6, 0, 0, 0]
