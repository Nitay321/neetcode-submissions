class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                l, r = i+1, len(nums)-1

                while l<r:
                    target = num + nums[l] + nums[r]

                    if target > 0:
                        r -= 1
                    elif target < 0:
                        l += 1
                    else:
                        res.append([num,nums[l],nums[r]])
                        l += 1

                        while nums[l] == nums[l-1] and l<r:
                            l+=1
        return res
                    

                 

        