class MinStack:

    def __init__(self):
        self.my_array = []

    def push(self, val: int) -> None:
        lowest = min(self.my_array[-1][1] if self.my_array else val, val)
        self.my_array.append((val, lowest))

    def pop(self) -> None:
        self.my_array.pop()

    def top(self) -> int:
        return self.my_array[-1][0]

    def getMin(self) -> int:
        return self.my_array[-1][1]
