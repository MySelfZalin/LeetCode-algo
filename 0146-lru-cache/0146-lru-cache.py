class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.nxt = None


class LRUCache:#от самого свежего к старому

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.nxt, self.right.prev = self.right, self.left


    def remove(self, node: Node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev
    

    def insert(self, node: Node):
        prev, nxt = self.left, self.left.nxt
        prev.nxt = nxt.prev = node
        node.prev, node.nxt = prev, nxt


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.right.prev
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)