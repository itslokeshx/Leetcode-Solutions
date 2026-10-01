class Codec:
    def serialize(self, root):
        queue=deque()
        if(root is None):
            return ""
        treestr=""
        treestr+=str(root.val)
        treestr+="#"
        queue.append(root)
        while queue:
            level_size=len(queue)
            for _ in range(0,level_size):
                removed=queue.popleft()
                if(removed.left):
                    queue.append(removed.left)
                    treestr+=str(removed.left.val)
                    treestr+="#"
                else:
                    treestr+="n#"
                if(removed.right):
                    queue.append(removed.right)
                    treestr+=str(removed.right.val)
                    treestr+="#"
                else:
                    treestr+="n#"
        return treestr
        
    def deserialize(self, data):
        if(data == ""):
            return
        queue=deque()
        strarr=data.split("#")[:-1]
        root=TreeNode(int(strarr[0]))
        queue.append(root)
        odd=1
        eve=2
        while queue:
            removed=queue.popleft()
            if(strarr[odd] != "n"):
                removed.left=TreeNode(int(strarr[odd]))
                queue.append(removed.left)
            if(strarr[eve] != "n"):
                removed.right=TreeNode(int(strarr[eve]))
                queue.append(removed.right)
            odd+=2
            eve+=2
        return root

            
        
        


        
            




        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))