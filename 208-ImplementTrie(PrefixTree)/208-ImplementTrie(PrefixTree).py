class MyTrie:
    def __init__(self):
        self.tr = [ [-1] * 26 ]
        self.isWord = [False]
        self.root = 0
        self.id = 1
    
    def init(self):
        self.root = 0
        self.id = 1
        self.tr = [ [-1] * 26 ]
        self.isWord = [False]
        
    def new_node(self):
        self.tr.append([-1] * 26)
        self.isWord.append(False)
        new_node = self.id
        self.id += 1
        return new_node
    
    def add(self, s):
        u = self.root
        for i in range(len(s)):
            c = ord(s[i]) - ord('a')
            if self.tr[u][c] == -1:
                self.tr[u][c] = self.new_node()
            u = self.tr[u][c]
        self.isWord[u] = True
    
    def find(self, s):
        u = self.root
        for i in range(len(s)):
            c = ord(s[i]) - ord('a')
            if u == -1:
                return -1
            u = self.tr[u][c]
        return u

class Trie:
    def __init__(self):
        self.trie = MyTrie()
        self.trie.init()

    def insert(self, word: str) -> None:
        self.trie.add(word)

    def search(self, word: str) -> bool:
        node = self.trie.find(word)
        return node != -1 and self.trie.isWord[node]

    def startsWith(self, prefix: str) -> bool:
        node = self.trie.find(prefix)
        return node != -1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)