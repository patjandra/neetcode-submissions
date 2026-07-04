class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}  # key -> DLL Node
        self.cap = capacity

        self.head = ListNode((0, 0))  # dummy LRU side
        self.tail = ListNode((0, 0))  # dummy MRU side

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.moveRecent(node)
        return node.val[1]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = (key, value)
            self.moveRecent(node)
        else:
            node = ListNode((key, value))
            self.cache[key] = node
            self.insertRecent(node)

            if len(self.cache) > self.cap:
                lru = self.head.next
                self.remove(lru)
                self.cache.pop(lru.val[0])

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertRecent(self, node):
        last = self.tail.prev

        last.next = node
        node.prev = last

        node.next = self.tail
        self.tail.prev = node

    def moveRecent(self, node):
        self.remove(node)
        self.insertRecent(node)


class ListNode:
    def __init__(self, val=(0, 0)):
        self.val = val  # (key, value)
        self.next = None
        self.prev = None