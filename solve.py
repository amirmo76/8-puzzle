from fringe import Stack, Queue, Fringe
from successor import successor
from node import Node
import time


def search_solution(init_node: Node, successor, fringe: Fringe):
    fringe.add(init_node)
    prev_depth = 0

    while len(fringe.data) > 0:
        candidate_node = fringe.get()
        if candidate_node.depth > prev_depth:
            print(f'finished depth {prev_depth}')
            prev_depth = candidate_node.depth
        if candidate_node.is_goal():
            return candidate_node
        for el in successor(candidate_node):
            fringe.add(el)
    return False


# ===============Testing=============
init_node = Node([[4, 1, 2], [7, 0, 3], [8, 5, 6]], 0)
f = Queue()
start_time = time.time()
result = search_solution(init_node, successor, f)
end_time = time.time()
if not result:
    print('Did not found any solution!')
else:
    print(result, f"in {end_time - start_time}s")
