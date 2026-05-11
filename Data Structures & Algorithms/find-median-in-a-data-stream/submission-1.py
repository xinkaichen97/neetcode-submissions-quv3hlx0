class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        if self.low and num < -self.low[0]:
            heapq.heappush(self.low, -num)
        else:
            heapq.heappush(self.high, num)
        if len(self.low) > len(self.high) + 1:
            val = -heapq.heappop(self.low)
            heapq.heappush(self.high, val)
        if len(self.high) > len(self.low) + 1:
            val = heapq.heappop(self.high)
            heapq.heappush(self.low, -val)

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            median = -self.low[0]
        elif len(self.high) > len(self.low):
            median = self.high[0]
        else:
            median = (-self.low[0] + self.high[0]) / 2
        return median
        