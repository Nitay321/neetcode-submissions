class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        Sum = 0
        for num in nums:
            Sum += num

        if Sum % 2 != 0:
            return False

        Sum /= 2
        memo = {}

        def find_sum(i, curr_sum):
            if curr_sum > Sum or i == len(nums):
                return False
            if curr_sum == Sum:
                return True

            if (i+1, curr_sum) not in memo:
                memo[(i+1, curr_sum)] = find_sum(i+1, curr_sum)
            if (i+1, curr_sum + nums[i]) not in memo:
                memo[(i+1, curr_sum + nums[i])] = find_sum(i+1, curr_sum + nums[i])

            memo[(i, curr_sum)] = memo[(i+1, curr_sum + nums[i])] or memo[(i+1, curr_sum)]
            return memo[(i, curr_sum)]

        return find_sum(0, 0)



        
            
        return find_sum(0,0)

            
            
            
            
            
            


         
            



            
