from Tree import Tree
from Problem import Problem

class MFC:
    problem: Problem = None
    X_domain: list[list[int]] = None
    X: list = None
    m: int = None

    def __init__(self, data_path, start_index) -> None:
        self.problem = Problem(data_path)

    
    def run(self):
        pass