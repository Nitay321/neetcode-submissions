class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in dictt:
                return [dictt[diff],i]
            dictt[num] = i
        