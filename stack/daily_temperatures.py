def daily_temperatures(temperatures):
    result = []
    for index, temp in enumerate(temperatures):
        index2 = index
        found = False
        while index2 < len(temperatures) - 1:
            index2 += 1
            if temperatures[index2] > temp:
                found = True
                break
        if found:
            result.append(index2 - index)
        else:
            result.append(0)
    return result


# ->
def daily_temperatures_optimal(temperatures):
    size = len(temperatures)
    result = [0] * size
    stack = []

    for index in range(size):
        while stack and stack[-1][0] < temperatures[index]:
            prev_t, prev_i = stack.pop()
            result[prev_i] = index - prev_i
        stack.append((temperatures[index], index))
    return result


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(daily_temperatures_optimal(temperatures))  # expected: [1, 1, 4, 2, 1, 1, 0, 0]
    print(daily_temperatures(temperatures))  # expected: [1, 1, 4, 2, 1, 1, 0, 0]


    temperatures = [30, 40, 50, 60]
    print(daily_temperatures(temperatures))  # expected: [1, 1, 1, 0]

    temperatures = [30, 60, 90]
    print(daily_temperatures(temperatures))  # expected: [1, 1, 0]

    temperatures = [90, 80, 70]
    print(daily_temperatures(temperatures))  # expected: [0, 0, 0]
