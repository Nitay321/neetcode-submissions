class Solution:
    def rob(self, nums: List[int]) -> int:
        def cal(lst):
            if len(lst) > 2:
                lst[2] += lst[0]
            for i in range(3,len(lst)):
                lst[i] += max(lst[i-2],lst[i-3])
            return max(lst[len(lst)-1],lst[len(lst)-2])

        if len(nums) == 1:
            return nums[0]
        nums2 = nums[1:]
        nums.pop()
        
        return max(cal(nums), cal(nums2))


    
    
            
          

        

        