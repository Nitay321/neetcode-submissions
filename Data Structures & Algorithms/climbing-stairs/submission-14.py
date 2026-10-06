class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        last_one_step = 2
        last_two_step = 1 
        
        for i in range(3,n+1):
            current_step = last_one_step + last_two_step
            last_two_step = last_one_step
            last_one_step = current_step
        return last_one_step

        