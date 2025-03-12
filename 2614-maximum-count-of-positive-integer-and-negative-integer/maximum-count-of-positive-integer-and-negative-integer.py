from bisect import bisect_left, bisect_right

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # given "nums" - sorted in increasing order
        # return max between numPos and numNeg
        numPos, numNeg = 0,0

        # for i in range(len(nums)):
        #     if nums[i] < 0:
        #         numNeg += 1
        #     elif nums[i] > 0:
        #         numPos += 1
 
        numNeg = bisect_left(nums, 0)
        numPos = len(nums) - bisect_right(nums, 0)

        return max(numPos, numNeg)


