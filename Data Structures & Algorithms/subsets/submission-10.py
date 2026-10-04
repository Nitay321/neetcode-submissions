class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []

        def subs(i):
            if i == len(nums):
                res.append(sub[:])
            else:
                sub.append(nums[i])
                subs(i+1)
                sub.pop()
                subs(i+1)

        subs(0)
        return res


        
        