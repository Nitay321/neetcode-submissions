class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = {}
        for c in s1:
            counter[c] = 1 + counter.get(c,0)

        
        l = 0
        for r,c in enumerate(s2):
            if c not in counter:
                while l != r:
                    counter[s2[l]] += 1
                    l += 1
                l += 1
            else:
                if counter[c] == 0:
                    while s2[l] != c:
                        counter[s2[l]] += 1
                        l += 1
                    l += 1
                else:
                    counter[c] -= 1
                    flag = True
                    for value in counter.values():
                        if value != 0:
                            flag = False
                            break
                    if flag:
                        return True
        return False



        