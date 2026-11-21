class Solution:
    def countBits(self, n: int) -> List[int]:

        def countN(n):
            count = 0
            while n>0:
                count += n % 2
                n = int(n/2) 
            return count
        
        res = []
        for i in range(n+1):
            res.append(countN(i))
        
        return res
 