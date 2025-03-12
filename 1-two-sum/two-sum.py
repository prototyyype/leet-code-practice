class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        numDict[nums[0]] = 0

        for i in range(1,len(nums)):
            comp = target-nums[i]
            if comp in numDict:
                return [numDict[comp],i]
            else:
                numDict[nums[i]]=i