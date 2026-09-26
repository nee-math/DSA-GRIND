def car_fleet(target, position, speed):
    data = sorted(zip(position, speed), reverse=True)

    stack = []
    for p, s in data:
        time = (target - p) / s
        if not stack:
            stack.append(time)
        else:
            last_time = stack[-1]
            if time <= last_time:
                continue
            else:
                stack.append(time)
    return len(stack)


if __name__ == '__main__':
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    print(car_fleet(target, position, speed))  # expected: 3

    target = 10
    position = [3]
    speed = [3]
    print(car_fleet(target, position, speed))  # expected: 1

    target = 100
    position = [0, 2, 4]
    speed = [4, 2, 1]
    print(car_fleet(target, position, speed))  # expected: 1

    target = 10
    position = [6, 8]
    speed = [3, 2]
    print(car_fleet(target, position, speed))  # expected: 2
