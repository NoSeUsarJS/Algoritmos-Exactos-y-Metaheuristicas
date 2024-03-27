class Node:
    value: int
    index: int
    solution: dict[int,int] = None
    parent = None
    child = None

    def __init__(self, X, index, solution) -> None:
        self.value = X
        self.index = index
        self.solution = solution