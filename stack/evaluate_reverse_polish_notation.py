def eval_rpn(tokens):
    operators = ["+", "/", "-", "*"]
    stack = []

    for t in tokens:
        if t in operators:
            first_operand = stack.pop()
            second_operand = stack.pop()
            value = apply_operator(second_operand, first_operand, t)
            stack.append(value)
        else:
            stack.append(int(t))
    if len(stack) == 1:
        return stack[-1]
    else:
        return Exception("Invalid RPN Notation")


def apply_operator(second, first, operation):
    match operation:
        case "+":
            return second + first
        case "-":
            return second - first
        case "/":
            if first == 0:
                return Exception("Cannot divide by 0")
            return int(second / first)
        case "*":
            return second * first
    return None


if __name__ == '__main__':
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(eval_rpn(tokens))  # expected: 22

    tokens = ["2", "1", "+", "3", "*"]
    print(eval_rpn(tokens))  # expected: 9

    tokens = ["4", "13", "5", "/", "+"]
    print(eval_rpn(tokens))  # expected: 6


