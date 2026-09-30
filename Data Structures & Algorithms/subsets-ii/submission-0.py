class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def subsets(i, sub):
            if i == len(nums):
                res.append(sub.copy())
            else:
                sub.append(nums[i])
                i+=1
                subsets(i, sub)
                sub.pop()
                while i < len(nums) and nums[i]==nums[i-1]:
                    i += 1
                subsets(i, sub)
                
        subsets(0,[])
        return res

