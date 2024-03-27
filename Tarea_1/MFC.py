from Tree import Tree
from Problem import Problem

class MFC:
    problem: Problem = None
    current_index: int = None
    X_domain: list[list[int]] = None
    X: list = None
    tree: Tree = None

    def __init__(self, data_path, start_index) -> None:
        self.problem = Problem(data_path)
        self.current_index = 0
        self.X_domain = [[0,1]] * self.problem.m
        self.tree = Tree(0, start_index, self.problem.m)
    
    def run(self):
        while self.current_index < self.problem.m:
            if self.current_index != self.tree.root.index:
                not_in_current_domain = []
                for value in self.X_domain[self.current_index]:
                    self.tree._add_child(value, self.current_index)
                    if self.problem._check_restrictions(self.tree.root.child.solution):
                        self.tree._fordward_to_child()
                        break
                    else:
                        not_in_current_domain.append(value)
                new_current_domain = list(set(self.X_domain[self.current_index]) - set(not_in_current_domain))
                if len(new_current_domain) == 0:
                    self.tree._back_to_parent()
                    self.tree.root.value += 1
                    if self.X_domain[self.current_index] > 1:
                        return {
                            "message" : "NO SOLUTION"
                        }
                else:
                    self.X_domain[self.current_index] = new_current_domain
                        
            self.current_index += 1