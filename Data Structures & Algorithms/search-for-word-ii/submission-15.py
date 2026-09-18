class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.childs = {}
        self.end_of_a_word = False

class TrieTree:
    def __init__(self):
        self.root = TrieNode()
        self.res = []
   
    def addWords(self, words):
        def insert(word):
            curr = self.root
            for char in word:
                if char not in curr.childs:
                    curr.childs[char] = TrieNode(char)
                curr = curr.childs[char]

            curr.end_of_a_word = True

        for word in words:
            insert(word)

    def searchWords(self,board):
        def searchPath(curr, board, visited, position,word):
            if curr.end_of_a_word:
                    self.res.append(word)
                    curr.end_of_a_word = False              
            i, j = position
            for char in curr.childs:
                newWord = word+char
                if i+1<len(board) and char == board[i+1][j] and (i+1,j) not in visited:
                    visited.append((i+1,j))
                    searchPath(curr.childs[char], board, visited,(i+1,j),newWord)
                    visited.pop()
                if j+1<len(board[0]) and char == board[i][j+1] and (i,j+1) not in visited:
                    visited.append((i,j+1))
                    searchPath(curr.childs[char], board, visited,(i,j+1),newWord)
                    visited.pop()
                if 0 <= i-1 and char == board[i-1][j] and (i-1,j) not in visited:
                    visited.append((i-1,j))
                    searchPath(curr.childs[char], board, visited,(i-1,j),newWord)
                    visited.pop()
                if 0 <= j-1 and char == board[i][j-1] and (i,j-1) not in visited:
                    visited.append((i,j-1))
                    searchPath(curr.childs[char], board, visited,(i,j-1),newWord)
                    visited.pop()
        curr = self.root
        for char in curr.childs: 
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == char:
                        searchPath(curr.childs[char], board, [(i,j)], (i,j), char)
    




class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = TrieTree()
        tree.addWords(words)
        tree.searchWords(board)
        return tree.res



        


        

            



        

        