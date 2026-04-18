class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        maxW = max(people)
        count = [0] * (maxW + 1)
        for p in people:
            count[p] += 1

        idx = 0
        for i in range(maxW + 1):
            while count[i] > 0:
                people[idx] = i
                idx += 1
                count[i] -= 1
        
        l, r = 0, len(people) - 1
        res = 0
        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l]:
                l += 1
        return res