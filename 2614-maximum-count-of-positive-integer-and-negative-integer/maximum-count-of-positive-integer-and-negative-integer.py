class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # given "nums" - sorted in increasing order
        # return max between numPos and numNeg
        numPos, numNeg = 0,0



        for i in range(len(nums)):
            if nums[i] < 0:
                numNeg += 1
            elif nums[i] > 0:
                numPos += 1


            # while nums[i] < 0:
            #     numNeg += 1
            #     i += 1
            # while nums[i] == 0:
            #     i += 1
            # while nums[i] > 0:
            #     numPos += 1
            #     i += 1
        
                


        return max(numPos, numNeg)