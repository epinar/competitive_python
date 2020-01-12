
from collections import defaultdict

class Trie:
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

def searchBoard(board, visited, trie, a, b, curr, res):

    for i,j in [(a-1,b), (a+1, b), (a, b-1), (a, b+1)]:
        if 0<=i<len(board) and 0<=j<len(board[0]):
            if visited[i][j] is 0:
                pr = curr + board[i][j]
                visited[i][j] = 1
                print(a, b, pr)
                if trie.startsWith(pr):
                    if trie.search(pr):
                        res.append(pr)
                    searchBoard(board, visited, trie, i, j, pr, res)
                visited[i][j] = 0
    return res

def findWords(board, words):

    ans = []

    trie = Trie()
    for word in words:
        trie.insert(word)

    vis = [[0]*len(board[0]) for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            vis[i][j]=1
            if trie.startsWith(board[i][j]):
                if trie.search(board[i][j]):
                    ans.append(board[i][j])
                else:
                    res = searchBoard(board, vis, trie, i, j, board[i][j], [])
                    for el in res:
                        ans.append(el)
            vis[i][j]=0

    return list(set(ans))



board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
print(findWords(board,words))

board = [
    ["a"]
]

words = ["a"]
print(findWords(board,words))

board = [["a","b"],["c","d"]]
words = ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]

print(findWords(board,words))
