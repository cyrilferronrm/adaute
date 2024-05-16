class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val}, {self.left}, {self.right})"


def preorder_traversal(root):
    if root is None:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)


def serialize(root):
    if root is None:
        return [None]
    return [root.val] + serialize(root.left) + serialize(root.right)


def deserialize(data):
    if not data:
        return None
    val = data.pop(0)
    if val is None:
        return None
    root = TreeNode(val)
    root.left = deserialize(data)
    root.right = deserialize(data)
    return root


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = None
    root.right = TreeNode(1)
    root.right.left = None
    root.right.right = None

    print(preorder_traversal(root))  # [1, None, 1, None]

    data = serialize(root)
    print(data)  # [1, None, 1, None, None]

    new_root = deserialize(data)
    print(preorder_traversal(new_root))  # [1, None, 1, None]
