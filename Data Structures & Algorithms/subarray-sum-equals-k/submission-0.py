class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = cursum = 0
        prefixSums = {0 : 1}

        for num in nums:
            cursum += num
            diff = cursum - k

            res += prefixSums.get(diff, 0)
            prefixSums[cursum] = 1 + prefixSums.get(cursum, 0)

        return res