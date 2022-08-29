class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def generateTrees(self, n):
        if n == 0:
            return []

        return self._generate(1, n)


    def _generate(self, start, end):

        if start > end:
            return [None]

        if start == end:
            return [TreeNode(start)]
        
        left = []
        right = []
        res = []
        for i in range(start, end+1):
            left = self._generate( start, i-1)
            right = self._generate( i+1, end)

            for j in left:
                for k in right:
                    root = TreeNode(i)
                    root.left = j
                    root.right = k
                    res.append(root)


        return res




solution = Solution()
print(solution.generateTrees(3))