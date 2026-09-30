class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def prem(sub):
            flag = False
            for num in nums:
                if num not in sub:
                    sub.append(num)
                    prem(sub)
                    sub.pop()
                    flag = True
            if not flag:
                res.append(sub.copy()) 
        prem([])
        return res


                    


           


            


        

        