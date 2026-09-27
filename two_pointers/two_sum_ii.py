def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum > target:
            right -=1
        else:
            left += 1
    return None


if __name__ == '__main__':
    numbers = [1, 2, 3, 4]
    target = 3
    print(two_sum(numbers, target))  # expected: [1, 2]

    numbers = [2, 7, 11, 15]
    target = 9
    print(two_sum(numbers, target))  # expected: [1, 2]

    numbers = [2, 3, 4]
    target = 6
    print(two_sum(numbers, target))  # expected: [1, 3]

    numbers = [-1, 0]
    target = -1
    print(two_sum(numbers, target))  # expected: [1, 2]

    numbers = [1, 1, 2, 3]
    target = 2
    print(two_sum(numbers, target))  # expected: [1, 2]

    numbers = [1, 3, 4, 5, 7, 10, 11]
    target = 9
    print(two_sum(numbers, target))  # expected: [3, 4]
