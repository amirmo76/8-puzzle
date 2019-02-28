class Fringe:
    data = list()

    def add(self, node):
        raise NotImplementedError("You haven't implemented this method")

    def get(self):
        raise NotImplementedError("You haven't implemented this method")


class Stack(Fringe):
    def add(self, node):
        self.data.append(node)

    def get(self):
        return self.data.pop()


class Queue(Fringe):
    def add(self, node):
        self.data.append(node)

    def get(self):
        node = self.data[0]
        self.data.remove(node)
        return node
