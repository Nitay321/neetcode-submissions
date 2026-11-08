class Solution:
    def jump(self, nums: List[int]) -> int:
            
        farthest = nums[0]
        limit_of_jump = 0 
        minJumps = 0

        for i in range(len(nums)-1):
            farthest = max(farthest ,i+nums[i])
            if i == limit_of_jump:
                minJumps += 1
                limit_of_jump = farthest
        
        return minJumps


        