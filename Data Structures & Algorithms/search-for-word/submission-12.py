class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        lst_string = []
        visit = []
        direction = [[1,0],[0,1],[-1,0],[0,-1]]

        def fun(i,j):
            if len(lst_string) == len(word):
                return True
            if not (-1<i<len(board) and -1<j<len(board[0])):
                return False
            if word[len(lst_string)] != board[i][j] or (i,j) in visit:
                return False
      

            lst_string.append(board[i][j])
            visit.append((i,j))

            for x,y in direction:
                x2, y2 = x + i, y + j
                if fun(x2,y2):
                    return True

            lst_string.pop()
            visit.pop()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if fun(i,j):
                    return True
        return False
        
            

            
                



            


            
                    

                
                


        