import math


def max_area(heights):
    """
    Given an integer array `heights` where heights[i] represents the height
    of the i-th bar, choose two bars that together with the x-axis form a
    container. Return the maximum amount of water it can store.

    The container cannot be slanted, so the water level is limited by the
    shorter of the two bars.
    """

    left, right = 0, len(heights) - 1
    result = 0

    while left < right:
        left_bar = heights[left]
        right_bar = heights[right]

        length = right - left
        area = min(left_bar, right_bar) * length

        result = max(area, result)

        if left_bar > right_bar:
            right -= 1
        else:
            left += 1
    return result

# Time complexiy O(N)
# Space complexity O(1)

if __name__ == '__main__':
    heights = [1, 7, 2, 5, 4, 7, 3, 6]
    print(max_area(heights))  # expected: 36

    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(max_area(heights))  # expected: 49

    heights = [1, 1]
    print(max_area(heights))  # expected: 1

    heights = [2, 2, 2]
    print(max_area(heights))  # expected: 4

    heights = [1, 2, 3, 4, 5]
    print(max_area(heights))  # expected: 6

    heights = [5, 1, 1, 1, 5]
    print(max_area(heights))  # expected: 20
