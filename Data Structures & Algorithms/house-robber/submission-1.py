class Solution:
    def rob(self, nums: List[int]) -> int:
        m = [-1]*(len(nums))
        
        def cal(i):
            if i >= len(nums):
                return 0
            n1 = cal(i+2) if i+2 >= len(nums) or m[i+2] == -1 else m[i+2]
            n2 = cal(i+3) if i+3 >= len(nums) or m[i+3] == -1 else m[i+3]
            n3 = cal(i+4) if i+4 >= len(nums) or m[i+4] == -1 else m[i+4]

            a = nums[i] + max(n1,n2)   
            b = 0 if i+1 >= len(nums) else nums[i+1] + max(n2,n3) 

            m[i] = max(a,b)

            return m[i]

        return cal(0)

        
