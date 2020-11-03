class BTree:

    def _init_(self):
        self.root = self.Node()

    class Node:
        def _init_(self):
            self.val = None
            self.left = None
            self.right = None

    def find_deepst(self):
        dps, _  = self.return_deepest(self.root, 0, self.root, 0)

        return dps

    def return_deepest(self, node, lvl, deepest, lvl_dps):

        if node is None:
            return deepest, lvl_dps

        deepest, lvl_dps = self.return_deepest(node.left, lvl+1, deepest, lvl_dps)

        if lvl_dps < lvl:
            deepest = node
            lvl_dps = lvl

        deepest, lvl_dps = self.return_deepest(node.right, lvl+1, deepest, lvl_dps)

        return deepest, lvl_dps


if __name__ == "__main__":
    tr = BTree()
    print(tr.root)







