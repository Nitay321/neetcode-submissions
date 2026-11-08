class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)-1
            
        farthest = nums[0]
        limit_of_jump = farthest 
        minJumps = 1

        for i in range(len(nums)-1):
            farthest = max(farthest ,i+nums[i])
            if i == limit_of_jump:
                minJumps += 1
                limit_of_jump = farthest
        
        return minJumps


        