class Solution:
    def reverseBits(self, n: int) -> int:
        bits = bin(n)[2:]
        length = 32 - len(bits)
        tmp = ['0']
        for i in range(len(bits)-1,-1,-1):
            tmp.append(bits[i])

        for _ in range(length):
            tmp.append('0')
        
        num_32 = "".join(tmp) 

        return int(num_32, 2)




        