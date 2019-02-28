import fringe
from successor import successor
from node import Node


def search_solution(init_node: Node, successor, fringe: fringe.Fringe):
    fringe.add(init_node)
    while len(fringe.data) > 0:
        candidate_node = fringe.get()
        if candidate_node.is_equal():
            return candidate_node
        for el in successor(candidate_node):
            fringe.add(el)
    return False


# ===============Testing=============
init_node = Node([[], [], []])
f = fringe.Stack()
result = search_solution(init_node, successor, f)
print(result)
