"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def count_unival_trees(root:Node):
    if root is None:
        return 0, True

    count_left, is_left_unival = count_unival_trees(root.left)
    count_right, is_right_unival = count_unival_trees(root.right)

    tot = count_left + count_right

    if is_left_unival and is_right_unival:
        if root.left is not None and root.data != root.left.data:
            return tot, False
        if root.right is not None and root.data != root.right.data:
            return tot, False
        return tot+1, True
    return tot, False

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(1)
    root.right = Node(0)
    root.right.left = Node(1)
    root.right.right = Node(0)
    root.right.left.left = Node(1)
    root.right.left.right = Node(1)

    cnt, _ = count_unival_trees(root)
    print(cnt)