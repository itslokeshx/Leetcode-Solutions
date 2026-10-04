"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned={}
        def dfs(node):
            if node is None:
                return 
            if( node in cloned):
                return cloned[node]
            x=Node(node.val)
            cloned[node]=x
            for i in node.neighbors:
                x.neighbors.append(dfs(i))
            return x
        return dfs(node)
            
        





        