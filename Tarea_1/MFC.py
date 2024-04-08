from Problem import Problem
from Node import Node
from os import system

class MFC:
    problem: Problem = None
    X_domain: list[list[int]] = None
    X: list = None
    m: int = None
    n: int = None
    max_FO_value: int = None
    nodes: list[Node] = []
    filtered_domain: list[list[int]] = None

    def __init__(self, data_path) -> None:
        self.problem = Problem(data_path)
        self.m = self.problem.m
        self.n = self.problem.n
        self.X_domain = [[1,0]] * self.m
        self.X = [0] * self.m
        self.max_FO_value = 0

    def _look_forward(self, entry_index, value, entry_dom: list):
        for j in range(entry_index+1, self.m):
            current_X = self.X[:]
            current_X[entry_index] = value
            current_dom = entry_dom
            for test_value in entry_dom[j]:
                current_X[j] = test_value
                system("cls")
                print(f"Max FO: {self.max_FO_value}")
                if self.problem._check_restrictions(current_X):
                    #CALCULAR FUNCIÓN OBJETIVO PARA CADA ELEMENTO
                    fo = self.problem._get_FO_value(current_X)
                    if self.max_FO_value < fo:
                        self.max_FO_value = fo
                        print(f"Max FO: {self.max_FO_value}")
                    return current_dom
                else:
                    current_dom[j].remove(test_value)
                    if not current_dom[j]:
                        return []

    def _mfc(self, entry_index, entry_dom, backtracking):
        if backtracking:
            entry_dom[entry_index] = [1]
        for value in entry_dom[entry_index]:
            new_dom = self._look_forward(entry_index=entry_index, value=value, entry_dom=entry_dom)
            if new_dom:
                #Return filtered domain
                return new_dom
        
        #Return empty list, cue to backtracking.
        return new_dom

    
    def run(self):
        next_domain = []
        for i in range(self.m):
            backtracking = True
            while backtracking:
                backtracking = False
                if i == 0 and not backtracking:
                    new_node = Node(i, self.X_domain)
                else:
                    new_node = Node(i, next_domain)
                self.nodes.append(new_node)
                new_dom = self._mfc(i, self.X_domain, backtracking=backtracking)
                if backtracking:
                    backtracking = False
                if new_dom:
                    next_domain = new_dom
                    self.filtered_domain = next_domain
                else:
                    #BACKTRACKING
                    i -= 1
                    if i < 0:
                        return []
                    self.nodes.pop()
                    next_domain = self.nodes[-1].dom
                    backtracking = True
        
        return self.filtered_domain

                




            
