# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      queue = deque()
      L=[]
      if root:
        queue.append(root)
      while len(queue) > 0:
        s=[]
        for i in range(len(queue)):
            curr = queue.popleft()
            s.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        L.append(s)
      return L 
        
