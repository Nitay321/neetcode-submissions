class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}

        for i,num in enumerate(nums):
            op = target - num
            if op in dictt:
                return [dictt[op], i]
            else:
                dictt[num] = i
         