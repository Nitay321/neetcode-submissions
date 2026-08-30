class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_index, l, r = 0, 0, len(nums)-1
        
        while l<=r:
            if nums[l]<nums[r] and nums[min_index] > nums[l]:
                min_index = l
                break
            m = (l + r) // 2
            
            if nums[m] < nums[min_index]:
                min_index = m

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        if min_index == 0:
                index = self.binary_search(nums,0,len(nums)-1, target)
                return index

        max_index = min_index - 1 

         
        if target < nums[min_index] or target > nums[max_index]:
            return -1

        print(min_index,len(nums)-1)
        index1 = self.binary_search(nums,0,max_index, target)           
        index2 = self.binary_search(nums,min_index,len(nums)-1, target)

        if index1 == -1:
            if index2 == -1:
                return -1
            else:
                return index2
        else:
            return index1     

    def binary_search(self,nums,l,r, target):
        while(l<=r):
            m = (l+r)//2
            if nums[m]>target:
                r = m - 1
            elif nums[m]<target:
                l = m + 1
            else:
                return m
            
        return -1


    
        