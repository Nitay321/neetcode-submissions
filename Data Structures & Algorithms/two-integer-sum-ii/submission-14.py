class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        while l<r:
            summ = nums[l]+nums[r]
            if summ < target:
                l+=1
            elif summ > target:
                r-=1
            else:
                return [l+1,r+1]
        return -1
        
        