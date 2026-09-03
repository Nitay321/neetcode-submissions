class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        res = nums[l]

        while l<=r:
            print(l,r)
            if nums[l]<=nums[r]:
                if nums[l] < res:
                    res = nums[l]
                break
            m = (l + r) // 2
            if nums[m] < res:
                res = nums[m]
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res