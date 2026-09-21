# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        def avglvl(node):
            queue = deque()
            avglist=[]
            if(node):
                queue.append(node)
            while queue:
                currlen=len(queue)
                avgval=0
                for i in range(currlen):
                    removed=queue.popleft()
                    avgval+=removed.val
                    if(removed.left):
                        queue.append(removed.left)
                    if(removed.right):
                        queue.append(removed.right)
                avglist.append(avgval/currlen)
            return avglist
        return avglvl(root)






        