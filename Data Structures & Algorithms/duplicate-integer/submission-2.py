class Solution:
   # def hasDuplicate(self, nums: List[int]) -> bool:
    #    seen = {}
     #   for num in nums:
      #      if num in seen:
       #         return True
        #    seen[num] = 0
        #return False
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums) 
    