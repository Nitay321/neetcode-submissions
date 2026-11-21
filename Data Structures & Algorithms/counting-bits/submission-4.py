class Solution:
    def countBits(self, n: int) -> List[int]:

        def countN(n):
            number = bin(n)
            count = 0
            for c in number:
                if c == '1':
                    count += 1
            return count
        
        res = []
        for i in range(n+1):
            res.append(countN(i))
        
        return res


    
        