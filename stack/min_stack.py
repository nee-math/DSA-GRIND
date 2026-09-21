class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        if not self.stack:
            self.stack.append(val)
            self.min_stack.append(val)
        else:
            last_min_val = self.min_stack[-1]
            if val > last_min_val:
                self.min_stack.append(last_min_val)
            else:
                self.min_stack.append(val)
            self.stack.append(val)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return None

    def get_min(self):
        return self.min_stack[-1]


if __name__ == '__main__':
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(min_stack.get_min())  # expected: -3
    min_stack.pop()
    print(min_stack.top())  # expected: 0
    print(min_stack.get_min())  # expected: -2
