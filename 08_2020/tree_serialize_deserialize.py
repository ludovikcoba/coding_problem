"""Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    if root == None:
        return "/"
    append_marker = "+"

    s = str(root.val)

    return s + append_marker + serialize(root.left) + append_marker + serialize(root.right)        

def deserialize(txt):

    values = iter(txt.split("+"))

    def deserializer():
        val = next(values)

        if val == "/":
            return None
        else:
            node = Node(val)
            node.left = deserializer()
            node.right = deserializer()
            return node

    return deserializer()




if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))

    print (serialize(node))
    print (deserialize(serialize(node)).left.left.val)
    #assert deserialize(serialize(node)).left.left.val == 'left.left'