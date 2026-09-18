class TrieNode:
    def __init__(self, char=''):
        self.char = char
        self.childs = {}
        self.end_of_a_word = False

class PrefixTree:

    def __init__(self, char=''):
        self.root = TrieNode()

    def insert(self, word: str) -> None: 
        curr = self.root 
        for char in word:
            if char not in curr.childs:
                curr.childs[char] = TrieNode(char)        
            curr = curr.childs[char]

        curr.end_of_a_word = True





    def search(self, word: str) -> bool:
        curr = self.root 
        for char in word:
            if char not in curr.childs:
                return False
            else:
                curr = curr.childs[char]
        return curr.end_of_a_word
            

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root 
        for char in prefix:
            if char not in curr.childs:
                return False
            else:
                curr = curr.childs[char]

        return True
            

