class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sub = []
        res = []
        def dfs(i, summ):
            if i > -1:                    
                if summ == target:
                    res.append(sub[:])
                elif summ < target:
                    sub.append(nums[i])
                    dfs(i, summ + nums[i])
                    sub.pop()
                    dfs(i - 1, summ)
        dfs(len(nums)-1, 0)
        return res
                



        