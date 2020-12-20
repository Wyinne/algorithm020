from collections import deque
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = []
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        queue =deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                root = queue.popleft()
                level.append(root.val)
                queue.extend(root.children)
            result.append(level)
        return result
n6=Node(6)
n5=Node(5)
n4=Node(4)
n3=Node(2)
n2=Node(3)
n1=Node(1)
n1.children=[n2,n3,n4]
n2.children=[n5,n6]
s=Solution()
result=s.levelOrder(n1)
print(result)