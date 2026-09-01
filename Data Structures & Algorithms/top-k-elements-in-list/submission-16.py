from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        m_c = counter.most_common(k)
        res = []
        for element in m_c:
            res.append(element[0])
        return res
        