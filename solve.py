from fringe import Stack, Queue, No_Repeat_Stack, Fringe
from successor import successor
from node import Node
import time


def search_solution(init_node: Node, successor, fringe: Fringe, depth_limit: int = 0):
    fringe.add(init_node)
    prev_depth = 0

    while len(fringe.data) > 0:
        candidate_node = fringe.get()
        if candidate_node.depth > prev_depth:
            print(f'finished depth {prev_depth}')
            prev_depth = candidate_node.depth
        if candidate_node.is_goal():
            return candidate_node
        if depth_limit and candidate_node.depth > depth_limit:
            continue
        for el in successor(candidate_node):
            fringe.add(el)
    return False


def iterative_depth_search_solution(init_node: Node, successor, depth_limit):
    this_round_depth_limit = 1
    f = No_Repeat_Stack()
    while this_round_depth_limit <= depth_limit:
        result = search_solution(init_node, successor,
                                 f, this_round_depth_limit)
        if result:
            return result
        this_round_depth_limit += 1
    return False


# ===============Testing=============
init_node = Node([[5, 3, 0], [6, 1, 8], [2, 4, 7]], 0)
f = No_Repeat_Stack()
start_time = time.time()
# result = search_solution(init_node, successor, f, 10)
result = iterative_depth_search_solution(init_node, successor, 20)
end_time = time.time()
if not result:
    print('Did not found any solution!')
else:
    print(result, f"in {end_time - start_time}s")
