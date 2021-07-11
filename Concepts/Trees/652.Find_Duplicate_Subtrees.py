def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        dic = collections.defaultdict(int)
        res = []
        
        def dfs(root):
            if not root:
                return '#'
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            s =  str(root.val) + ',' + left + ',' + right
            
            dic[s] += 1
            
            if dic[s] == 2:
                res.append(root)

            return s
                
        dfs(root)
        return res