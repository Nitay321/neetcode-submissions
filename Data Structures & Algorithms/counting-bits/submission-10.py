class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        k = 1
        res = [0]
        while k<=n:
            count = res[k >> 1] + (k & 1)
            res.append(count)
            k+=1
        return res

        