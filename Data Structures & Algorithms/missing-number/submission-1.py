class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsS= 0
        summ = 0

        for n in nums:
            numsS += n

        for i in range(1,len(nums)+1):
            summ += i

        print (summ, numsS)
        return summ - numsS
         