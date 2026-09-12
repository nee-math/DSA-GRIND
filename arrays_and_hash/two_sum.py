def two_sum(nums, target):
    storage = {}

    for index, num in enumerate(nums):
        print(storage)
        remainder = target - num
        if remainder in storage:
            return [storage.get(remainder), index]

        storage[num] = index

    return []



# Time O(N)
# Space O(N)


if __name__ == '__main__':
    nums = [4,5,6]
    target = 11
    print(two_sum(nums, target))
