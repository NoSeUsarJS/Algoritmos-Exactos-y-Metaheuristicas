class Node:
    values: dict
    parent = None
    children: list = []

    def __init__(self, X, Y) -> None:
        self.values = {
            "X": X,
            "Y": Y
        }
    
    def _get_child(self, index):
        return self.children[index]

    def _get_parent(self):
        return self.parent