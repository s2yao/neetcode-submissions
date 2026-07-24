class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        # need a locating system
        locate = {}
        # record curr visited node
        visited = set()

        # gets node from locate arr
        def get_node(number) -> Node:
            if number not in locate:
                new_node = Node(number, [])
                locate[number] = new_node
            return locate[number]
        
        process = [node]
        visited.add(node)
        while process:
            curr_node = process.pop()
            new_curr_node = get_node(curr_node.val)
            # visited.add(curr_node)

            for neighbor_node in curr_node.neighbors:
                # create new node
                new_neighbor_node = get_node(neighbor_node.val)
                # append to new_curr_node
                new_curr_node.neighbors.append(new_neighbor_node)
                # add original node if not visited
                if neighbor_node not in visited:
                    process.append(neighbor_node)
                    visited.add(neighbor_node)
        return locate[1]



