class Solution:

  def hasDuplicate(self, nums: List[int]) -> bool:
    seen = set()
    for num in nums:
      if num in seen:
        return True
      seen.add(num)
    return False

  # Alternative 1: Dictionary approach
  # def hasDuplicate(self, nums: List[int]) -> bool:
  #     seen = {}
  #     for num in nums:
  #         if num in seen:
  #             return True
  #         seen[num] = 0
  #     return False

  # Alternative 2: One-liner set approach
  # def hasDuplicate(self, nums: List[int]) -> bool:
  #     return len(set(nums)) < len(nums)