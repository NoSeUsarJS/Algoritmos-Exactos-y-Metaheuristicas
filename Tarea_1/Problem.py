from functools import lru_cache

class Problem:
    #Number of projects
    m: int = None

    #Number of tasks
    n: int = None

    #Maximum budget
    B: int = None
    
    #Profits of each project
    g: list[int] = None

    #Costs of each task.
    c: list[int] = None

    #Tasks associated with each project
    T: list[list[bool]] = []

    #Number of tasks associated with each project
    NT: list[int] = []
            

    def __init__(self, dataPath: str) -> None:
        with open(dataPath, "r") as data:
            data = open(dataPath, "r")

            self.m = int(data.readline())
            self.n = int(data.readline())
            self.B = int(data.readline())
            project_profits_line = data.readline()
            tasks_costs_line = data.readline()

            self.g = project_profits_line.split(" ")
            #Removes the last element, which is "\n".
            self.g.pop()
            self.g = list(map(int, self.g))
            self.c = tasks_costs_line.split(" ")
            #Removes the last element, which is "\n".
            self.c.pop()
            self.c = list(map(int, self.c))

            remaining_lines = data.readlines()

            for line in remaining_lines:
                row = line.split(" ")
                #Removes the last element, which can be "\n" or "".
                row.pop()
                row = list(map(int, row))
                self.NT.append(sum(row))
                self.T.append(row)
    
    def _get_parameters(self):
        print(f"m = {self.m}")
        print(f"n = {self.n}")
        print(f"B = {self.B}")
        print(f"g = {self.g}")
        print(f"c = {self.c}")
        print(f"NT = {self.NT}")
        #print(f"T = {self.T}")

    def _check_restrictions(self, X: list, Y: list) -> bool:
        sum_Y_and_c = sum([a * b for a, b in zip(Y, self.c)])

        if sum_Y_and_c > self.B:
            return False

        for i in range(self.m):
            sum_T_and_Y = sum([a * b for a, b in zip(self.T[i], Y)])
            for k in range(self.n):
                if self.T[i][k] * Y[k] != X[i]:
                    return False
                if self.NT[i] * X[i] != sum_T_and_Y:
                    return False
                
        return True

    def _get_FO_value(self, X: list):
        FO_value = sum([a * b for a, b in zip(X, self.g)])
        return FO_value