class Solution:
    def countBits(self, n: int) -> List[int]:
        
        if n == 0:
            return [0]
        
        res = [0]
        mul = 1
        k = 1

        while k <= n:
            res.append(1 + res[k-mul])
            if k == mul:
                mul *= 2
            k += 1
        return res


       