
from collections import defaultdict

class Trie:

    def __init__(self):
        self.prefs = defaultdict()

    def insert(self, word):
        for i in range(len(word)):
            pr = word[:i]
            print(pr)
            if pr not in self.prefs:
                self.prefs[pr]=0
        self.prefs[word]=1

    def search(self, word):
        return word in self.prefs and self.prefs[word]==1

    def startsWith(self, prefix):
        return prefix in self.prefs

class Trie2:
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t['#'] = '#'

    def search(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                return False
            t = t[w]
        if '#' in t:
            return True
        return False

    def startsWith(self, prefix):
        t = self.trie
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        return True

obj = Trie()
obj.insert("ab")
print(obj.search("a"))
print(obj.startsWith("a"))

obj.insert("apple")
print(obj.search("apple"))
print(obj.startsWith("app"))
obj.insert("app")
print(obj.search('app'))
# param_3 = obj.startsWith(prefix)