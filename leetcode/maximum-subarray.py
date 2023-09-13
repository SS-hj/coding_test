class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -1e9
        temp = 0
        for n in nums:
            temp += n
            res = max(res, temp)
            if temp < 0:
                temp = 0
        return res