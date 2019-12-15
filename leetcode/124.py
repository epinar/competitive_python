

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxPathSum(root):
    ### Calculate two paths: one that is from left child node, root and to right node.
    ### The other is max of left or right paths and the root node itself.
    def recurse(node):
        if not node:
            return [float('-inf')]*2
        left = recurse(node.left)
        right = recurse(node.right)
        #print('left:', left+right)
        return [node.val + max(left[0], right[0], 0),
                max(left + right + [node.val + left[0] + right[0]])]
    res = recurse(root)
    print(res)
    return max(res)

def maxPathSum2(root):
    max_val = 0
    def recurse(node):
        if not node:
            return 0
        left = recurse(node.left)
        right = recurse(node.right)
        max_val = max(max_val, left+node.val + right)
        return max(node.val + max(left, right), 0)

    recurse(root)
    return max_val

#root = TreeNode(5)
#root.left = TreeNode(2)
#root.right = TreeNode(3)
#print(maxPathSum(root))

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(maxPathSum(root))

#root = TreeNode(2)
#root.left = TreeNode(-1)
#print(maxPathSum(root))