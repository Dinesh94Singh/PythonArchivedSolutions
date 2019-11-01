def get_char_index(c):
    return ord(c) - ord('a')


class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.size = 0

    def get_node(self, c):
        child = self.children[get_char_index(c)]
        return child

    def set_node(self, c, node):
        self.children[get_char_index(c)] = node

    def add(self, s, index):
        self.size += 1
        if index == len(s):
            return
        current = s[index]
        child = self.get_node(current)
        if not child:
            child = TrieNode()
            self.set_node(current, child)
        child.add(s, index + 1)

    def add_string(self, s):
        self.add(s, 0)

    def find_count(self, s, index):
        if len(s) == index:
            return index
        child = self.get_node(s[index])
        if not child:
            return 0
        return child.find_count(s, index + 1)


node = TrieNode()
node.add_string(list('sing'))
print(node.children)
print(node.children[ord('s')-ord('a')].children)
print(node.find_count('sing', 0))
