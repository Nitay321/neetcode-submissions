class Solution:
    def hammingWeight(self, n: int) -> int:
        number = bin(n)
        count = 0
        for c in number:
            if c == '1':
                count+=1
        return count
        