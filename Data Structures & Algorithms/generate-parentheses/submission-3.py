class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        twoN = 2*n
        res = []
        def fun(l, r, string_lst):
            print(l,r)
            if l == r and l+r == twoN:
                string = "".join(string_lst)
                res.append(string)
            elif r <= l and l+r < twoN:
                string_lst.append("(")
                fun(l+1, r, string_lst)
                string_lst.pop()
                string_lst.append(")")
                fun(l, r+1, string_lst)
                string_lst.pop()
            
        fun(0,0,[])
        return res



        