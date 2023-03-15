class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxNum, minNum = 0, prices[0]
        for p in prices:
            if minNum > p:
                minNum = p
            elif p-minNum > maxNum:
                maxNum = p-minNum
        return maxNum