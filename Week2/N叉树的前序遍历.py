class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children =[]
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])
        return output
n6=Node(6)
n5=Node(5)
n4=Node(4)
n3=Node(2)
n2=Node(3)
n1=Node(1)
n1.children=[n2,n3,n4]
n2.children=[n5,n6]
s=Solution()
result=s.preorder(n1)
print(result)
