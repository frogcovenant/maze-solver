from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        """Adds a child node to the current node"""
        self.children.append(child_node)

    def remove_child(self, child_node):
        """Removes a child node from the current node"""
        self.children = [child for child in self.children if child != child_node]

    def bfs(self):
        """Performs Breadth-First Search (BFS) traversal"""
        queue = deque([self])
        nodes = []
        
        while queue:
            current_node = queue.popleft()
            nodes.append(current_node.value)
            queue.extend(current_node.children)
        
        return nodes
    
    def solve(self, goal):
        """Solves a 2D maze represented with a TreeNode start and a given goal"""
        # Queue for BFS, stores tuples of (current node, path to reach there)
        queue = deque([(self, [self.value])])

        while queue:
            current_node, path = queue.popleft()

            # If we reached the goal, return the path
            if current_node.value == goal:
                return path

            # Enqueue the children nodes
            for child in current_node.children:
                queue.append((child, path + [child.value]))

        # If no path is found, return None
        return None
    
    def __repr__(self, level=0):
        """Recursive __repr__ to display the tree structure"""
        ret = "  " * level + f"TreeNode(value={self.value})\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret