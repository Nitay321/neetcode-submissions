class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        current_jump_end = 0
        minJumps = 0
        
        for i in range(len(nums) - 1): 
            farthest = max(farthest, i + nums[i])

            if i == current_jump_end:
                minJumps += 1               
                current_jump_end = farthest  

        return minJumps