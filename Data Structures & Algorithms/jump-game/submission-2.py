class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        possible = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] + i >= possible:
                possible = i
        
        if possible == 0:
            return True

        return False

            
        

