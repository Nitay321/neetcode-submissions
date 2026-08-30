from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums).most_common(k)
        result = []
        for num,key in counter:
            result.append(num)
        return result