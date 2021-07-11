"""
208. Implement a Trie

https://leetcode.com/problems/implement-trie-prefix-tree/solution/

"""

"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""


class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.word = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.word = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.word

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True


"""
["Trie","insert","search","search","startsWith","insert","search"]
[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]

Expected - [null,null,true,false,true,null,true]
"""
trie = Trie()
print(None)
print(trie.insert("apple"))
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
print(trie.insert("app"))
print(trie.search("app"))
print('\n\n\n')
"""
["Trie","insert","search","search","search","startsWith","startsWith","startsWith"]
[[],["hello"],["hell"],["helloa"],["hello"],["hell"],["helloa"],["hello"]]

Expected - [null,null,false,false,true,true,false,true]
"""

trie = Trie()
print(None)
print(trie.insert("hello"))
print(trie.search("hell"))
print(trie.search("helloa"))
print(trie.search("hello"))
print(trie.startsWith("hell"))
print(trie.startsWith("helloa")) # expected to be false
print(trie.startsWith("hello"))
print('\n\n\n')
"""
["Trie","insert","search","startsWith"]
[[],["a"],["a"],["a"]]

Expected - [null,null,true,true]
"""
trie = Trie()
print(trie.insert("a"))
print(trie.search("a"))
print(trie.startsWith("a"))