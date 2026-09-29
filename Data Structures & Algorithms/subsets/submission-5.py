class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def subsets(nums, sub, i):
            if i == -1:
                res.append(sub[:])

            else:
                sub.append(nums[i])
                subsets(nums, sub, i - 1)
                sub.pop()
                subsets(nums, sub, i - 1)
        
        subsets(nums, [], len(nums)-1)
        return res

       