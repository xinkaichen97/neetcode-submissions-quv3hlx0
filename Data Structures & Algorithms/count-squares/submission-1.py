class CountSquares:

    def __init__(self):
        self.points = []
        self.mp = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points.append(point)
        self.mp[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x0, y0 = point
        res = 0
        for x, y in self.points:
            if x == x0 or y == y0 or abs(x - x0) != abs(y - y0):
                continue
            res += self.mp[(x0, y)] * self.mp[(x, y0)]
        return res




