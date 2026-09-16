class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)
        for f in range(len(nums)-2):
            if nums[f] > 0:
                break
            if f>0 and nums[f-1] == nums[f]:
                continue
            s, t = f+1, len(nums)-1
            while s<t:
                if nums[s] == -1 and nums[f] == -1:
                    print(nums[t])
                sumOfThree = nums[f]+nums[s]+nums[t]
                if sumOfThree <= 0:
                    if sumOfThree == 0:
                        res.append([nums[f],nums[s],nums[t]])
                    s += 1
                    while nums[s-1] == nums[s] and s<t:
                        s += 1          
                else:
                    t -= 1            
        return res
                




            
        