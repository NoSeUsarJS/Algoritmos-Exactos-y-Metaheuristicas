from Tree import Tree
from Problem import Problem

class MFC:
    tree: Tree = None
    problem: Problem = None
    

    def __init__(self, data_path, start_X) -> None:
        self.tree = Tree(start_X)
        self.problem = Problem(data_path)
    
    def run(self):
        #Step 1
        pass
