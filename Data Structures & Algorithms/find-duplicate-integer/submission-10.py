from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = Counter(nums)
        number, f = counter.most_common(1)[0]
        return number
        

        