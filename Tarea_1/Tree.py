from Node import Node

class Tree:
    root: Node
    max_height: int = None
    values_list: list = None

    def __init__(self, X, index, max_height):
        solution = {}
        solution[index] = X
        new_node = Node(X, index, solution)
        self.root = new_node
        self.max_height = max_height
    
    def _set_child(self, X, index):
        solution = self.root.solution
        solution[index] = X
        new_node = Node(X, index, solution)
        new_node.parent = self.root
        self.root.child.append(new_node)
    
    def _fordward_to_child(self):
        self.root = self.root.child
    
    def _back_to_parent(self):
        self.root = self.root.parent
    
