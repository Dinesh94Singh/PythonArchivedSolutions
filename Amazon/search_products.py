class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.data = None
        self.is_end = False


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def create_Trie(self, word_dict):
        for each_word in word_dict:
            self.add_word(each_word)

    def add_word(self, word):
        p = self.root
        for ch in word:
            if ch in p.children:
                pass
            else:
                p.children[ch] = TrieNode()
            p = p.children[ch]

        p.is_end = True
        p.data = word

    def dfs(self, root):
        res = []
        if root:
            if root.is_end:
                res.append(root.data)
            for child in root.children:
                res.extend(self.dfs(root.children[child]))
            return res

    def search(self, keyword):
        p = self.root
        for ch in keyword:
            if ch in p.children:
                p = p.children[ch]
            else:
                return []
        return self.dfs(p)

    def search_products(self, word_dict, word):
        self.create_Trie(word_dict)
        res = []
        for i in range(1, len(word)):
            keyword = word[:i + 1]
            filtered_words = self.search(keyword)
            res.append([filtered_words[:3]])
        return res


s = Solution()
print(s.search_products(['mouse', 'mousepad', 'money', 'moneypot', 'dinesh'], 'mouse'))
