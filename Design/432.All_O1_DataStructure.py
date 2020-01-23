class DoubleyLLNode:
    def __init__(self, val, prev = None, nxt = None):
        self.val = val
        self.prev = prev
        self.nxt = nxt

        self.freq = 0

class DoubleLL:
    def __init__(self):
        self.head = DoubleyLLNode(None)
        self.tail = DoubleyLLNode(None)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

class AllOne:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.freq_to_list = {}
        self.key_to_node = {}

        self.max_key_val = float('-inf')
        self.min_key_val = float('inf')
        
    def __remove_node(self, key):
        """
        * Removes the node from key-to-node map
        * Removes the freq if no nodes in that freq list
        """
        node = self.key_to_node[key]
        prev = node.prev
        nxt = node.next

        if prev:
            prev.next = nxt
        if nxt:
            nxt.prev = prev

        dll = self.freq_to_list[key]
        dll.size -= 1

        if dll.size == 0:
            del self.freq_to_list[key]
            del dll

    def __add_node(self, new_freq, node):
        """
        * Adds the node into key-to-node map
        * Increments the size of dll of the new freq
        """
        dll = self.freq_to_list[new_freq]
        
        tail = dll.tail
        prev_node = tail.prev
        if prev_node:
            prev_node.next = node
        if node:
            node.prev = prev_node
            node.nxt = tail
        tail.prev = node

        node.freq = new_freq
        dll.size += 1

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        prev_freq = 0
        node = DoubleyLLNode(key)
        if key in self.key_to_node:
            node = self.key_to_node[key]
            prev_freq = node.freq
            self.__remove_node(key)
        
        new_freq = prev_freq + 1

        if new_freq not in self.freq_to_list:
            self.freq_to_list[new_freq] = DoubleLL()

        self.__add_node(new_freq, node)
        

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.freq_to_list:
            return -1
        
        node = self.key_to_node[key]
        prev_freq = node.freq

        new_freq = prev_freq - 1

        if new_freq not in self.freq_to_list:
            self.freq_to_list[new_freq] = DoubleLL()
        
        self.__remove_node(prev_freq)
        self.__add_node(new_freq, node)
        
        

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        self.max_key_val if self.max_key_val != float('-inf') else -1
        

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        self.min_key_val if self.min_key_val != float('inf') else -1
        


# Your AllOne object will be instantiated and called as such:
obj = AllOne()
obj.inc(5)
obj.inc(5)
print(obj.getMaxKey())
print(obj.getMinKey())