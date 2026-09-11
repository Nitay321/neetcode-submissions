class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        minN = nums[l]
        while l<=r:
            if nums[l] <= nums[r]:
                minN = min(minN, nums[l])
                break
            else:
                m = (l + r) // 2
                if nums[l] <= nums[m]:
                    l = m + 1
                else:             
                    r = m - 1

                    minN = min(minN, nums[m])
        return minN

            
        