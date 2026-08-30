class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        # הלולאה רצה כל עוד המצביעים לא נפגשו
        while l < r:
            m = (l + r) // 2
            
            # אם האמצע גדול מהימין - המינימום חייב להיות מימינו
            if nums[m] > nums[r]:
                l = m + 1
            
            # אם האמצע קטן מהימין - המינימום הוא האמצע או משמאלו
            else:
                r = m
                
        # כשהלולאה מסתיימת, l ו-r מצביעים לאותו מקום - שהוא המינימום
        return nums[l]