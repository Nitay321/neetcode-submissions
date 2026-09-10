from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            counter[num] = counter.get(num,0) + 1

        freq = defaultdict(list)

        for key in counter:
            freq[counter[key]].append(key)

        print(freq)
        i =len(nums)
        res = []
        while k>0 and i>0:
            if not freq[i]:
                i -= 1
            else:
                res.append(freq[i].pop())
                k -= 1
        return res

            
            


        