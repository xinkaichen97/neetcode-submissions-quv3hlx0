class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        times = self.mp[key]
        l, r = 0, len(times) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if times[m][0] <= timestamp:
                res = times[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
