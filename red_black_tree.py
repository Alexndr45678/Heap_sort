class Tree:
    class Node:
        def __init__(self, value=None, color=None, left=None, right=None):
            self.value = value
            self.color = color
            self.left = left
            self.right = right

    class Color:
        RED = 0
        BLACK = 1

    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is not None:
            result = self.add_node(self.root, value)
            self.root = self.rebalance(self.root)
            self.root.color = self.Color.BLACK
            return result
        else:
            self.root = self.Node(value=value, color=self.Color.BLACK)
            return True

    def add_node(self, node, value):
        if node.value == value:
            return False
        else:
            if node.value > value:
                if node.left is not None:
                    result = self.add_node(node.left, value)
                    node.left = self.rebalance(node.left)
                    return result
                else:
                    node.left = self.Node(value=value, color=self.Color.RED)
                    return True
            else:
                if node.right is not None:
                    result = self.add_node(node.right, value)
                    node.right = self.rebalance(node.right)
                    return result
                else:
                    node.right = self.Node(value=value, color=self.Color.RED)
                    return True

    def rebalance(self, node):
        result = node
        need_rebalance = True
        while need_rebalance:
            need_rebalance = False
            if (
                result.right is not None
                and result.right.color == self.Color.RED
                and (result.left is None or result.left.color == self.Color.BLACK)
            ):
                need_rebalance = True
                result = self.right_swap(result)
            if (
                result.left is not None
                and result.left.color == self.Color.RED
                and result.left.left is not None
                and result.left.left.color == self.Color.RED
            ):
                need_rebalance = True
                result = self.left_swap(result)
            if (
                result.left is not None
                and result.left.color == self.Color.RED
                and result.right is not None
                and result.right.color == self.Color.RED
            ):
                need_rebalance = True
                self.color_swap(result)
        return result

    def color_swap(self, node):
        node.right.color = self.Color.BLACK
        node.left.color = self.Color.BLACK
        node.color = self.Color.RED

    def right_swap(self, node):
        right_child = node.right
        between_child = right_child.left
        right_child.left = node
        node.right = between_child
        right_child.color = node.color
        node.color = self.Color.RED
        return right_child

    def left_swap(self, node):
        left_child = node.left
        between_child = left_child.right
        left_child.right = node
        node.left = between_child
        left_child.color = node.color
        node.color = self.Color.RED
        return left_child

    def print_tree(self):
        self._print_tree(self.root)
        
    def _print_tree(self, node):
        if node:
            self._print_tree(node.left)
            if node.color == 1:
                print(f"Black -> {node.value}")
            else:
                print(f"Red -> {node.value}")
            self._print_tree(node.right)

tree = Tree()
tree.add(5)
tree.add(10)
tree.add(15)
tree.add(7)
tree.add(4)
tree.add(9)
tree.add(6)
tree.print_tree()