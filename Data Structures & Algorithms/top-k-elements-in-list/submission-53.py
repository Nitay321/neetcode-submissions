from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt = defaultdict(int)
        for num in nums:
            dictt[num] += 1
        
        counter = defaultdict(list)
        for key in dictt:
            value = dictt[key]
            counter[value].append(key)
        
        res = []
        r = len(nums)
        count = 0
        print(counter)
        while count < k:
            if not counter[r]:
                r-=1
            else:
                val = counter[r].pop()
                res.append(val)
                count += 1    
        return res
            
