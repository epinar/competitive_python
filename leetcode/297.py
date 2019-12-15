import queue


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        res = []
        nodes = queue.Queue()
        nodes.put(root)
        while not nodes.empty():
            n = nodes.get()
            if n != None:
                nodes.put(n.left)
                nodes.put(n.right)
                res.append(str(n.val))
            else:
                res.append('null')

        # remove nulls from the end of the list

        #while res[-1]== 'null':
        #    res = res[:-1]

        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if len(data)==0:
            return None

        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = queue.Queue()
        q.put(root)
        ind = 1
        while not q.empty():
            n = q.get()
            if nodes[ind] != 'null':
                n.left = TreeNode(int(nodes[ind]))
                q.put(n.left)
            ind += 1

            if nodes[ind] != 'null':
                n.right = TreeNode(int(nodes[ind]))
                q.put(n.right)

            ind += 1

        return root


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
s = codec.serialize(root)
root2 = codec.deserialize(s)

