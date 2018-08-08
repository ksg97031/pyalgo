class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def __repr__(self):
        nf = lambda node: "Node {}".format(node.data) if node is not None else "Empty"
        return "{} <-- {} --> {}".format(
            nf(self.left), nf(self), nf(self.right))

    def insert(self, data):
        assert type(data) is type(self.data)
        if data < self.data:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = Node(data)
        elif data > self.data:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = Node(data)
        else:
            pass  # exists

    def find(self, data):
        assert type(data) is type(self.data)
        if data < self.data:
            if self.left is not None:
                return self.left.find(data)
            return None
        elif data > self.data:
            if self.right is not None:
                return self.right.find(data)
            return None
        else:
            return self


if __name__ == '__main__':
    node = Node(3)
    node.insert(3)
    node.insert(4)
    node.insert(9)
    b = node.find(9)
    if b:
        print("[Success] Founded Node : " + str(node.find(3)))
