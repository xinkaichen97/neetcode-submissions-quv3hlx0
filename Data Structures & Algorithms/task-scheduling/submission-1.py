class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        heap = []
        q = deque()
        counts = {}

        for task in tasks:
            counts[task] = counts.get(task, 0) + 1
        for count in counts.values():
            heapq.heappush(heap, -count)
        
        currTime = 0
        while q or heap:
            currTime += 1
            if not heap:
                currTime = q[0][0]
            else:
                count = -heapq.heappop(heap) - 1
                if count > 0:
                    q.append((currTime + n, count))
            if q and q[0][0] == currTime:
                heapq.heappush(heap, -q.popleft()[1])

        return currTime


            