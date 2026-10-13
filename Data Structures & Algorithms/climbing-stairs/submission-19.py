class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        one = 1
        two = 2 
        for _ in range(2,n):
            tmp = two
            two = one + two
            one = tmp
        
        return two