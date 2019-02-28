class Node:
    parent_node = None
    state = [[0 for i in range(3)] for j in range(3)]

    def __init__(self, state):
        self.state = state

    def diff(self, node) -> list:
        # return [i for i, j in zip(self.state, node.state) if i == j]
        return [i for i, j in zip(self.state, node.state) if i == j]

    def is_equal(self, node) -> bool:
        return True if self.diff(node) else False
