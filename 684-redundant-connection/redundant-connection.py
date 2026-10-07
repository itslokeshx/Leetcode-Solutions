class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:

        parent=[]

        for i in range(len(edges)+1):
            parent.append(i)
        
        def find(x):
            while parent[x] != x:
                x=parent[x]
            return x

        for a,b in edges:
            
            root_a=find(a)
            root_b=find(b)

            if(root_a == root_b):
                return [a,b]

            parent[root_b]=root_a

        return []


            

        