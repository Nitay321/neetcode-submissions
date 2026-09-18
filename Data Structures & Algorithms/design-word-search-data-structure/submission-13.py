class TrieNode:
    def __init__(self, char=''):
        self.char = char
        self.childs = {}
        self.end_of_a_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()  

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.childs:
                curr.childs[char] = TrieNode(char)

            curr = curr.childs[char]
        curr.end_of_a_word = True
  
    def search(self, word: str) -> bool:
        
        def deep_search(word, node):            
            curr = node
            for i,char in enumerate(word):
                if char == '.':
                    for c in curr.childs:
                        if deep_search(word[i+1:],curr.childs[c]):
                            return True
                    return False
                elif char not in curr.childs:
                    return False
                else:
                    curr = curr.childs[char]
            return curr.end_of_a_word


        return deep_search(word,self.root)

        
