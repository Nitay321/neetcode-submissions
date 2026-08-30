class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = nums[0]

        while l<=r:
            if nums[l]<nums[r]:
                res = min(nums[l], res)
                return res
            m = (l + r) // 2
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
            
            res = min(nums[m], res)

        return res


        


#    1 2 3 4 5
#    5 1 2 3 4
#    4 5 1 2 3
#    3 4 5 1 2
#    2 3 4 5 1
        
#   7 8 0 1 2 3 4 5 6