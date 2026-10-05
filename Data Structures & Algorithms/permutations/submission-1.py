class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = []
        res = []
        def pre():
            if len(nums) == len(visited):
                res.append(visited[:])
            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                visited.append(nums[i])
                pre()
                visited.pop()
        pre()
        return res






        
        
        