class Node:
    parent_node = None
    state = [[0 for i in range(3)] for j in range(3)]

    def __init__(self, state):
        self.state = state

    def diff(self, node) -> list:
        return [i for i, j in zip(self.state, node.state) if i == j]

    def is_equal(self, node) -> bool:
        return True if len(self.diff(node)) == len(self.state) else False

    def is_goal(self):
        return self.is_equal(Node([[1, 2, 3], [4, 5, 6], [7, 8, 0]]))
