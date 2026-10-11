class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dictt = collections.defaultdict(int)

        for num in nums:
            dictt[num] += 1
        
        freqs = [[] for _ in range(len(nums)+1)]
        for num, freq in dictt.items():
            freqs[freq].append(num)

        res = []
        for i in range(len(freqs)-1,-1,-1):
            while freqs[i]:
                e = freqs[i].pop()
                res.append(e)
                k -= 1
                if k==0:
                    return res
        return res


        

            

        





