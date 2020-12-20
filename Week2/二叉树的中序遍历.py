class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
           self.val = val
           self.left = left
           self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[]
        res=[]
        while (stack or root):
            if root:
                stack.append(root)
                root=root.left
            else:
                temp=stack.pop()
                root=temp.right
                res.append(temp.val)
        return res
a=Solution()
b=TreeNode()
d=a.inorderTraversal(b)
print(d)
