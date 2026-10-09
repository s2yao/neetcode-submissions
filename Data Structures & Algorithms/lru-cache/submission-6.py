class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.dict_map = {}
        self.cap = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if self.cap == 0:
            return
        # key dne
        if key not in self.dict_map:
            return -1

        # get node val
        curr_node = self.dict_map[key]

        # delete original node
        curr_prev = curr_node.prev
        curr_next = curr_node.next
        curr_prev.next = curr_next
        curr_next.prev = curr_prev

        # put node to front of ll
        curr_head = self.head.next
        self.head.next = curr_node
        curr_node.next = curr_head
        curr_head.prev = curr_node
        curr_node.prev = self.head

        # return val
        return curr_node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        # put new nodeto front
        new_node = Node(key, value)
        curr_head = self.head.next
        self.head.next = new_node
        new_node.next = curr_head
        curr_head.prev = new_node
        new_node.prev = self.head

        # put a key that already exist
        if key in self.dict_map:
            # deletion of key
            curr_node = self.dict_map[key]
            curr_prev = curr_node.prev
            curr_next = curr_node.next
            curr_prev.next = curr_next
            curr_next.prev = curr_prev
        # putting key require eviction
        elif self.cap == len(self.dict_map):
            curr_node = self.tail.prev
            curr_prev = curr_node.prev
            curr_next = curr_node.next
            curr_prev.next = curr_next
            curr_next.prev = curr_prev
            del self.dict_map[curr_node.key]
            
        # update dict
        self.dict_map[key] = new_node

