class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            elif i>0 and nums[i-1]==nums[i]:
                continue
            else:
                j = i+1
                k = len(nums)-1
                while j<k:
                    sumThree = nums[i]+nums[j]+nums[k]
                    if sumThree<0:
                        j+=1
                    elif sumThree>0:
                        k-=1
                    else:
                        res.append([nums[i],nums[j],nums[k]])
                        j+=1
                        while j<k and nums[j-1]==nums[j]:
                            j+=1
        return res


                
