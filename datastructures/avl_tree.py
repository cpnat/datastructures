from datastructures.node import AVLTreeNode


class AVLTree:

    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root) if self.root is not None else ''

    def __insert_recursion(self, node, val):
        if node is None:
            return AVLTreeNode(val, None, None)

        if val < node.val:
            node.left = self.__insert_recursion(node.left, val)
        elif val > node.val:
            node.right = self.__insert_recursion(node.right, val)
        elif val == node.val:
            raise ValueError('Value already contained within tree')

        node.height = max(AVLTree.node_height(node.left), AVLTree.node_height(node.right)) + 1

        return AVLTree.node_balance(node)

    def insert(self, val):
        self.root = self.__insert_recursion(self.root, val)

    def __depth_recursion(self, node, depth=0):
        if node is None:
            return depth

        left = self.__depth_recursion(node.left, depth + 1)
        right = self.__depth_recursion(node.right, depth + 1)
        return max(left, right)

    def depth(self):
        if self.root is None:
            return -1
        else:
            return self.__depth_recursion(self.root)

    @staticmethod
    def node_height(node):
        return node.height if node is not None else -1

    @staticmethod
    def node_balance_factor(node):
        if node is None:
            return 0
        else:
            return AVLTree.node_height(node.left) - AVLTree.node_height(node.right)

    @staticmethod
    def node_is_left_heavy(balance_factor):
        return balance_factor > 1

    @staticmethod
    def node_is_right_heavy(balance_factor):
        return balance_factor < -1

    @staticmethod
    def node_rotate_left(node):

        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        new_root.height = AVLTree.node_height(new_root)
        node.height = AVLTree.node_height(node)
        return new_root

    @staticmethod
    def node_rotate_right(node):

        new_root = node.left
        node.left = new_root.right

        new_root.height = AVLTree.node_height(new_root)
        node.height = AVLTree.node_height(node)
        return new_root

    @staticmethod
    def node_balance(node):
        balance_factor = AVLTree.node_balance_factor(node)

        if AVLTree.node_is_left_heavy(balance_factor):
            if AVLTree.node_balance_factor(node.left) < 0:
                node.left = AVLTree.node_rotate_left(node.left)
            node = AVLTree.node_rotate_right(node)

        elif AVLTree.node_is_right_heavy(balance_factor):
            if AVLTree.node_balance_factor(node.right) > 0:
                node.right = AVLTree.node_rotate_right(node.right)
            node = AVLTree.node_rotate_left(node)

        return node
