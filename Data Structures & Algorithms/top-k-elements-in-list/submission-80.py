
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
        
        lst = [[] for _ in range(len(nums)+1)]
        for key,value in counter.items():
            lst[value].append(key)
        
        res = []
        for i in range(len(lst)-1,0,-1):
            while lst[i]:
                if k == 0:
                    return res
                element = lst[i].pop()
                res.append(element)
                k -= 1

        return res


        