class MyQueue:

    def __init__(self):
        self.q_in = []
        self.q_out = []

    def push(self, x: int) -> None:
        self.q_in.append(x)

    def pop(self) -> int:
        self.peek()
        return self.q_out.pop()

    def peek(self) -> int:
        if not self.q_out:
            while self.q_in:
                self.q_out.append(self.q_in.pop())
        return self.q_out[-1]

    def empty(self) -> bool:
        return not (self.q_in or self.q_out)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()