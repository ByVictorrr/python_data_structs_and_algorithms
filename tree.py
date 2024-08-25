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

    def __str__(self, level=0, prefix="Root: "):
        ret = " " * (4 * level) + prefix + f"Node({self.data})\n"
        if self.left_child is not None:
            ret += self.left_child.__str__(level + 1, prefix="L--- ")
        if self.right_child is not None:
            ret += self.right_child.__str__(level + 1, prefix="R--- ")
        return ret

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


def insert_into_bst_tree(root, data):
    """Insert a node with somewhere in the Binary Search Tree depending on the data."""
    if not root:
        return BinaryTreeNode(data)
    if data == root.data:
        raise RuntimeError(f"Value {data} already in the BST.")

    if data < root.data:
        root.left_child = insert_into_bst_tree(root.left_child, data)
    else:
        root.right_child = insert_into_bst_tree(root.right_child, data)
    return root


def search_in_bst(root, value):
    """Search for the value in a node in the Binary Search Tree."""
    if not root:
        return False
    elif root.data == value:
        return True
    elif root.data > value:
        return search_in_bst(root.left_child, value)
    else:
        return search_in_bst(root.right_child, value)


def delete_in_bst(root, value):
    """Delete a node in the bst that has a value of."""
    # Base case: if the tree is empty
    if not root:
        return None
    # Recursive case: traverse the tree to find the node to delete
    if root.data > value:
        root.left_child = delete_in_bst(root.left_child, value)
    elif root.data < value:
        root.right_child = delete_in_bst(root.right_child, value)
    else:
        # Node Found: this is the node to be deleted
        # Case1: Node has no child (node is a leaf node)
        if not root.left_child and not root.right_child:
            return None
        # Case 2: Node has only one child
        if not root.left_child:
            return root.right_child
        if not root.right_child:
            return root.left_child
        # Case 3: Node has two children
        # Find the in-order successor's value (smallest val in the right subtree)
        # Find the minimum value in the right subtree
        current = root.right_child
        while not current.left_child:
            current = current.left_child
        successor = current
        # Replace the nodes value with the successors value
        root.data = successor.data
        # Delete the successor
        root.right = delete_in_bst(root.right, successor.value)

    return root


def find_max_depth(root):
    if not root:
        return 0
    left_depth = find_max_depth(root.left_child)
    right_depth = find_max_depth(root.right_child)
    return max(left_depth, right_depth) + 1


def find_min_depth(root):
    if not root:
        return 0
    if not root.left_child and not root.right_child:
        return 1
    if not root.left_child:
        return find_min_depth(root.right_child) + 1
    if not root.right_child:
        return find_max_depth(root.left_child) + 1
    return min(find_max_depth(root.left_child), find_max_depth(root.right_child)) + 1


if __name__ == "__main__":
    root_node = insert_into_bst_tree(None, 50)
    for val in [20, 53, 11, 22, 52, 78]:
        insert_into_bst_tree(root_node, val)
    print(root_node)
    in_order(root_node)
