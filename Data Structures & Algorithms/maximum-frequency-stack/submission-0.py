class FreqStack:

    def __init__(self):
        self.stacks = {}
        self.counts = {}
        self.maxCount = 0

    def push(self, val: int) -> None:
        valCount = self.counts.get(val, 0) + 1
        self.counts[val] = valCount
        if valCount > self.maxCount:
            self.maxCount = valCount
            self.stacks[valCount] = []
        self.stacks[valCount].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxCount].pop()
        self.counts[res] -= 1
        if not self.stacks[self.maxCount]:
            self.maxCount -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()