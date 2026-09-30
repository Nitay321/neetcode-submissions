class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x,y,sub,visited,i):
            if i == len(word):
                return False
            if sub[i] != word[i]:
                return False
            if len(word) == len(sub):
                return True

            a,b,c,d = False,False,False,False
            if -1 < x + 1 < len(board) and (x+1,y) not in visited:
                visited.append((x+1,y))
                sub.append(board[x+1][y])
                a = dfs(x+1,y,sub,visited,i+1)
                sub.pop()
                visited.pop()
            if -1 < x - 1 < len(board) and (x-1,y) not in visited:
                visited.append((x-1,y))
                sub.append(board[x-1][y])
                b = dfs(x-1,y,sub,visited,i+1)
                sub.pop()
                visited.pop() 
                
            if -1 < y + 1 < len(board[0]) and (x,y+1) not in visited:
                visited.append((x,y+1))
                sub.append(board[x][y+1])
                c = dfs(x,y+1,sub,visited,i+1)
                sub.pop()
                visited.pop()
            if -1 < y - 1 < len(board[0]) and (x,y-1) not in visited:
                visited.append((x,y-1))
                sub.append(board[x][y-1])
                d = dfs(x,y-1,sub,visited,i+1)
                sub.pop()
                visited.pop()

            return a or b or c or d
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if dfs(x,y,[board[x][y]],[(x,y)],0):
                    return True
        return False

                

            

        