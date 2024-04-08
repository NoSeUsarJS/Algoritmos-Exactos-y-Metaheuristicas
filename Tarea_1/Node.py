class Node:
    index: int = None
    dom: list[list[int]] = None

    def __init__(self, index, dom) -> None:
        self.index = index
        self.dom = dom