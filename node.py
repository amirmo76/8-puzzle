class Node:
    parent_node_id = 0
    node_id = 0
    state = [[0 for i in range(3)] for j in range(3)]
    depth = 0

    def __init__(self, state, id=0):
        self.state = state
        self.node_id = id

    def diff(self, node) -> list:
        return [i for i, j in zip(self.state, node.state) if i == j]

    def is_equal(self, node) -> bool:
        return True if len(self.diff(node)) == len(self.state) else False

    def is_goal(self):
        return self.is_equal(Node([[1, 2, 3], [4, 5, 6], [7, 8, 0]]))

    def __str__(self):
        return "id:" + str(self.node_id) + " ,state:" + self.state.__str__() + " ,depth:" + str(self.depth)

    def __repr__(self):
        return self.__str__()
