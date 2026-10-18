# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue=deque()
        res=[]
        if root :
            queue.append(root)
        while len(queue)>0:
            b=len(queue)-1
            for i in range(len(queue)):
                curr=queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                if i==b:
                    res.append(curr.val)


        return res

