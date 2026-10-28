class Trie():

    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                cur.children[c] = Trie()
                cur = cur.children[c]

        cur.isWord = True
            

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                if word[i] == ".":
                    for char in cur.children.values():
                        if dfs(i + 1, char):
                            return True

                    return False

                elif word[i] not in cur.children:
                    return False

                else:
                    cur = cur.children[word[i]]

            return cur.isWord

        return dfs(0, self.root)
            
