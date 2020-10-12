from dataclasses import dataclass


@dataclass
class CacheNode:
    key: int = 0
    val: int = 0
    prev: 'CacheNode' = None
    next: 'CacheNode' = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.list = None

        self.head = CacheNode()
        self.tail = CacheNode
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _remove_tail(self):
        last = self.tail.prev
        self._remove_node(last)
        return last

    def get(self, key: int):
        node = self.cache.get(key)
        if node is None:
            return -1
        self._move_to_front(node)
        return node.val

    def put(self, key: int, val: int):
        node = self.cache.get(key)
        if node is None:
            node = CacheNode(key, val)
            if self.size >= self.capacity:
                last = self._remove_tail()
                del self.cache[last.key]
                self.size -= 1

            self._add_node(node)
            self.cache[key] = node
            self.size += 1

        else:
            self._move_to_front(node)
            node.val = val
