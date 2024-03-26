class Node:
    values: dict
    parent = None
    children: list = []

    def __init__(self, X) -> None:
        self.values = X