class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        nums.sort()
        def dfs(i, summ):
            if summ == target:
                res.append(sub.copy())
            elif i > -1 and summ < target:
                sub.append(nums[i])
                dfs(i - 1, summ+nums[i])
                sub.pop()
                while i > 0 and nums[i] == nums[i-1]:
                    i -= 1
                dfs(i - 1, summ)

        dfs(len(nums)-1, 0)
        return list(res)

        