class Trinode:
    def __init__(self):
        self.children={}
        self.wordend=False
class WordDictionary:

    def __init__(self):
        self.root=Trinode()

        

    def addWord(self, word: str) -> None:
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=Trinode()
            node=node.children[char]
        node.wordend=True
        

    def search(self, word: str) -> bool:
        def dfs(index,node):
            curr=node
            for i in range(index,len(word)):
                char=word[i]
                if char==".":
                    for  child  in curr.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr=curr.children[char]
            return curr.wordend
        return dfs(0,self.root)




        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)