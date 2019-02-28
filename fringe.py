from node import Node


class Fringe:
    data = list()

    def add(self, node: Node):
        raise NotImplementedError("You haven't implemented this method")

    def get(self):
        raise NotImplementedError("You haven't implemented this method")


class Stack(Fringe):
    def add(self, node: Node):
        self.data.append(node)

    def get(self):
        return self.data.pop()


class Queue(Fringe):
    def add(self, node: Node):
        self.data.append(node)

    def get(self):
        node = self.data[0]
        self.data.remove(node)
        return node


class No_Repeat_Stack(Stack):
    def add(self, node: Node):
        for i in self.data:
            if node.is_equal(i):
                return
        super().add(node)
