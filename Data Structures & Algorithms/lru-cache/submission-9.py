class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.key_to_node = {}
        self.cap = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        
        curr_node = self.key_to_node[key]
        ret = curr_node.val

        curr_next = curr_node.next
        curr_prev = curr_node.prev
        curr_prev.next = curr_next
        curr_next.prev = curr_prev

        curr_head = self.head.next
        self.head.next = curr_node
        curr_node.next = curr_head
        curr_head.prev = curr_node
        curr_node.prev = self.head

        return ret

    def put(self, key: int, value: int) -> None:
        # if key already exist - delete node
        if key in self.key_to_node:
            curr_node = self.key_to_node[key]
            curr_next = curr_node.next
            curr_prev = curr_node.prev
            curr_prev.next = curr_next
            curr_next.prev = curr_prev
        
        # create new node
        new_node = Node(key, value)
        # add to front
        curr_head = self.head.next
        self.head.next = new_node
        new_node.next = curr_head
        curr_head.prev = new_node
        new_node.prev = self.head

        # update dictionary
        self.key_to_node[key] = new_node

        # if limit reached - evict
        curr_cap = len(self.key_to_node)
        # print(curr_cap, self.cap)
        if curr_cap > self.cap:
            curr_tail = self.tail.prev
            curr_next = curr_tail.next
            curr_prev = curr_tail.prev
            curr_prev.next = curr_next
            curr_next.prev = curr_prev
            del self.key_to_node[curr_tail.key]
