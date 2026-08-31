class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = {}
        for c in s1:
            counter[c] = 1 + counter.get(c,0)
     
        subL = 0
        l = 0

        for r in range(len(s2)):
            if s2[r] not in counter:
                # מקרה 1: תו שלא קיים ב-s1. 
                # מחזירים את כל המונים למצבם הקודם ומאפסים את החלון
                while l < r:
                    counter[s2[l]] += 1
                    l += 1
                l += 1 # מקדמים את l צעד אחד מעבר לתו הלא-תקין הנוכחי
                subL = 0

            elif counter[s2[r]] == 0: # תוקן: בודקים אם הגענו ל-0
                # מקרה 2: יש לנו יותר מדי מהתו הזה. 
                # מקווצים משמאל עד ש"נזרוק" את המופע הקודם שלו.
                while s2[r] != s2[l]:
                    counter[s2[l]] += 1
                    subL -= 1 # תוקן: מעדכנים את האורך בהתאם
                    l += 1
                
                # אנחנו עוצרים בדיוק על התו הכפול, אז צריך לדלג גם עליו!
                # שים לב: אנחנו כאילו "זורקים" אותו מצד שמאל, ו"מכניסים" 
                # אותו מצד ימין (r), ולכן המונה ו-subL לא משתנים בשלב הזה.
                l += 1

            else:
                # מקרה 3: הכל תקין, מכניסים את התו לחלון
                counter[s2[r]] -= 1
                subL += 1
                if subL == len(s1):
                    return True
                    
        return False