from queue import Queue
from dataclasses import dataclass


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []

    def left_children(self):
        if (num_children := len(self.children)) == 0:
            return []
        return self.children[:num_children // 2]

    def right_children(self):
        if (num_children := len(self.children)) == 0:
            return []
        return self.children[num_children // 2:]


class BinaryTreeNode(TreeNode):

    def __init__(self, data):
        super().__init__(data)
        self.children.extend([None, None])  # Initialize with two None values

    @property
    def left_child(self):
        return self.children[0]

    @left_child.setter
    def left_child(self, node):
        if len(self.children) < 2:
            self.children.append(None)  # Ensure we have two slots
        self.children[0] = node

    @property
    def right_child(self):
        return self.children[1]

    @right_child.setter
    def right_child(self, node):
        if len(self.children) < 2:
            self.children.append(None)  # Ensure we have two slots
        self.children[1] = node


def preorder(root):
    if not root:
        return
        # print root node
    print(root.data)
    if len(root.children) == 2:
        preorder(root.left_child)
        preorder(root.right_child)
    else:
        for lc in root.left_children:
            preorder(lc)
        for rc in root.right_children:
            preorder(rc)


def post_order(root):
    if not root:
        return
    if len(root.children) == 2:
        post_order(root.left_child)
        post_order(root.right_child)
    else:
        for lc in root.left_children:
            post_order(lc)
        for rc in root.right_children:
            post_order(rc)
    print(root.data)


def level_order(root):
    q = Queue()
    q.put(root)
    while not q.empty():
        if not (node := q.get()):
            continue
        print(node.data)
        if len(root.children) == 2:
            q.put(node.left_child)
            q.put(node.right_child)
        else:
            for lc in root.left_children:
                q.put(lc)
            for rc in root.right_children:
                q.put(rc)


def in_order(root):
    if not root:
        return
    if len(root.children) == 2:
        in_order(root.left_child)
        print(root.data)
        in_order(root.right_child)
    else:
        for lc in root.left_children:
            in_order(lc)
        print(root.data)
        for rc in root.right_children:
            in_order(rc)


def insert_into_bt_tree(root, data):
    """Insert a node with somewhere in the bt tree depending on the data."""
    if not root:
        return BinaryTreeNode(data)
    if data < root.data:
        root.left_child = insert_into_bt_tree(root.left_child, data)
    else:
        root.right_child = insert_into_bt_tree(root.right_child, data)
    return root


if __name__ == "__main__":
    root_node = insert_into_bt_tree(None, 50)
    for val in [20, 53, 11, 22, 52, 78]:
        insert_into_bt_tree(root_node, val)
    in_order(root_node)
