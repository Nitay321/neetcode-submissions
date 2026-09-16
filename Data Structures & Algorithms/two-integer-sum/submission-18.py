class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}
        for i, num in enumerate(nums):
            ops = target - num
            if ops in dictt:
                return [dictt[ops],i]

            dictt[num] = i
    
            


        