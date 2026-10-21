class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        Sum = 0
        for num in nums:
            Sum += num

        if Sum % 2 != 0:
            return False

        Sum /= 2
        dictt = {}

        def find_sum(i, curr_sum):
            if curr_sum > Sum:
                return False
            if curr_sum == Sum:
                return True
            if i == len(nums):
                return False

            ans1 = find_sum(i + 1, curr_sum + nums[i]) if (i+1, curr_sum + nums[i]) not in dictt else dictt[(i+1, curr_sum + nums[i])]

            ans2 = find_sum(i + 1, curr_sum) if (i + 1, curr_sum) not in dictt else dictt[(i+1, curr_sum)]

            dictt[(i,curr_sum)] =  ans1 or ans2
            return dictt[(i,curr_sum)]

        return find_sum(0,0)

            
            
            
            
            
            


         
            



            
