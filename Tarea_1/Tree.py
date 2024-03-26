from Node import Node

class Tree:
    root: Node = None

    def __init__(self, X):
        new_node = Node(X)
        self.root = new_node
    
    def _add_child(self, X):
        new_node = Node(X)
        new_node.parent = self.root
        self.root.children.append(new_node)
    
    def _get_child(self, index):
        return self.root.children[index]
    
    def _fordward_to(self, index):
        self.root = self.root.children[index]
    
    def _back_to_parent(self):
        self.root = self.root.parent
    
