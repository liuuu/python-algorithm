class BST:
  def isBST(self, root):
    def helper(node, lower, upper):
      if not node:
        return True

      val = node.value
      if val < lower or val >= upper:
        return False

      if not helper(node.left, lower, val):
        return False
      if not helper(node.right, val, upper):
        return False

      return True

    return helper(root, float('-inf'), float('inf'))


class TreeNode:
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None


#  10
# 5   12
# 2 6

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(12)
root.left.right = TreeNode(6)
root.left.left = TreeNode(2)
print(BST().isBST(root))
