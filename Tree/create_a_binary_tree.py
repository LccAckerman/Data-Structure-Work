# define a node
class Node(object):
    def __init__(self, val=None):
        self.value = val
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_value(self, val):
        self.value = val

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None


class Tree:
    def __init__(self, val):
        self.root = Node(val)

    def get_root(self):
        return self.root


# check


node0 = Node("apple")
node1 = Node("banana")
node2 = Node("orange")

print(f"has left child? {node0.has_left_child()}")
print(f"has right child? {node0.has_right_child()}")

print("adding left and right children")
node0.set_left_child(node1)
node0.set_right_child(node2)

print(f"has left child? {node0.has_left_child()}")
print(f"has right child? {node0.has_right_child()}")
