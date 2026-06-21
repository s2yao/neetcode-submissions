class Node:
    def __init__(self, val: int, key: int):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        # ll to keep track of the elements
        self.dummyhead = Node(0, 0)
        # dict to have O(1) retrieval of nodes
        self.key_to_node = {}
        # key to the back most node to evict
        self.backmost = -1
        # capacity
        self.max_capacity = capacity
        # curr_capacity
        self.curr_capacity = 0

    def get(self, key: int) -> int:
        # update curr key node to front
        if key not in self.key_to_node:
            return -1
        curr_node = self.key_to_node[key] 

        # backmost handle
        if key == self.backmost and curr_node.prev != self.dummyhead:
            self.backmost = curr_node.prev.key

        if self.dummyhead.next and self.dummyhead.next != curr_node:
            # update around curr_node
            curr_node.prev.next = curr_node.next
            if curr_node.next:
                curr_node.next.prev = curr_node.prev
            # update dummy head
            head_node = self.dummyhead.next
            if head_node:
                curr_node.next = head_node
                head_node.prev = curr_node
            self.dummyhead.next = curr_node
            curr_node.prev = self.dummyhead

        return self.key_to_node[key].val

    def put(self, key: int, value: int) -> None:
        # if key already exists, update value and move to front
        if key in self.key_to_node:
            curr_node = self.key_to_node[key]
            curr_node.val = value
            self.get(key)
            return

        # check curr_capacity
        if self.curr_capacity == self.max_capacity:
            self.evict()

        # curr node
        curr_node = Node(value, key)

        # append to head
        head_node = self.dummyhead.next
        if head_node:
            curr_node.next = head_node
            head_node.prev = curr_node
        self.dummyhead.next = curr_node
        curr_node.prev = self.dummyhead

        # append curr_node to dictionary
        self.key_to_node[key] = curr_node

        # backmost handle
        if self.curr_capacity == 0:
            self.backmost = key
        
        self.curr_capacity += 1


    def evict(self) -> bool:
        # locate back most node
        back_most_node = self.key_to_node[self.backmost]
        if back_most_node.prev == self.dummyhead:
            self.backmost = -1
        else:
            self.backmost = back_most_node.prev.key
        back_most_node.prev.next = None
        back_most_node.prev = None
        del self.key_to_node[back_most_node.key]
        self.curr_capacity -= 1