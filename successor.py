from node import Node
from copy import deepcopy


def move(node: Node, dir: str, index: tuple) -> Node:
    new_node = deepcopy(node)
    new_node.parent_node = node
    if dir == 'left':
        temp = node.state[index[0]][index[1] - 1]
        new_node.state[index[0]][index[1] - 1] = 0
        new_node.state[index[0]][index[1]] = temp
    elif dir == 'right':
        temp = node.state[index[0]][index[1] + 1]
        new_node.state[index[0]][index[1] + 1] = 0
        new_node.state[index[0]][index[1]] = temp
    elif dir == 'up':
        temp = node.state[index[0] - 1][index[1]]
        new_node.state[index[0] - 1][index[1]] = 0
        new_node.state[index[0]][index[1]] = temp
    else:
        temp = node.state[index[0] + 1][index[1]]
        new_node.state[index[0] + 1][index[1]] = 0
        new_node.state[index[0]][index[1]] = temp
    return new_node


def successor(node: Node):
    index = (-1, -1)
    for row in node.state:
        try:
            index = (node.state.index(row), row.index(0))
        except:
            continue
    if index[0] == -1 or index[1] == -1:
        raise RuntimeError('0 was not found')

    generated_nodes = []

    if index[1] > 0:
        # generate left move
        generated_nodes.append(move(node, 'left', index))
    if index[1] < len(node.state[0]) - 1:
        # generate right move
        generated_nodes.append(move(node, 'right', index))
    if index[0] > 0:
        # generate up move
        generated_nodes.append(move(node, 'up', index))
    if index[0] < len(node.state) - 1:
        # generate bottom move
        generated_nodes.append(move(node, 'bottom', index))
    return generated_nodes
