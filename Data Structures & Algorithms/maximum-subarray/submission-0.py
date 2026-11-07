class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxS = nums[0]
        summ = maxS 
        for i in range(1,len(nums)):
            summ = max(summ + nums[i], nums[i])
            maxS = max(maxS, summ)
        
        return maxS
            
        