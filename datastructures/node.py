class TreeNode:

    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return '{{val={}, left={}, right={}}}'.format(self.val, self.left, self.right)


class AVLTreeNode(TreeNode):

    def __init__(self, val, left, right):
        super().__init__(val, left, right)
        self.height = 0

    def __str__(self):
        return '{{val={}, height={}, left={}, right={}}}'.format(self.val, self.height, self.left, self.right)

