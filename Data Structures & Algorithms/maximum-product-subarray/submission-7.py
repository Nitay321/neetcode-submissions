class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = nums[0], nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            tempMax = nums[i] * currMax
            currMax = max(nums[i], tempMax, nums[i] * currMin)
            currMin = min(nums[i], tempMax, nums[i] * currMin)
            res = max(res, currMax)
        
        return res
            

