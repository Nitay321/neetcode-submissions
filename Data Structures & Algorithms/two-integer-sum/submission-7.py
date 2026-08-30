class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        op = {}
        for i, num in enumerate(nums):
            opposite = target - num
            if opposite in op:
                return [op[opposite], i]
            op[num] = i
         
        