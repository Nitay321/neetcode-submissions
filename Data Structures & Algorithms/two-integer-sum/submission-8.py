class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ops = {}
        for i,num in enumerate(nums):
            key = target - num
            if key in ops:
                return [ops[key], i]
            ops[num] = i
        
        
