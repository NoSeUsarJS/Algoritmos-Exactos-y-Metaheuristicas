from Tree import Tree
from Problem import Problem

class MFC:
    tree: Tree = None
    problem: Problem = None

    def __init__(self, data_path, start_X, start_Y) -> None:
        self.tree = Tree(start_X, start_Y)
        self.problem = Problem(data_path)
    
    def _run():
        pass

    
