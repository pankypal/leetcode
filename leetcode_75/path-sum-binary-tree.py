# 437. Path Sum III


# Given the root of a binary tree and an integer targetSum, return the number of paths where the 
# sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf, but it must go downwards 
# (i.e., traveling only from parent nodes to child nodes).

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pathSum1(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """

        if not root:
            return 0
        
        return self._pathSum1(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
    
    def _pathSum1(self, root, targetSum):
        if not root:
            return 0
        
        res = 1 if root.val == targetSum else 0
        res += self._pathSum1(root.left, targetSum - root.val) + self._pathSum1(root.right, targetSum - root.val)

        return res
    
    def pathSum(self, root, targetSum):
        prefixSums = {}

        return self._pathSum(root, 0, targetSum, prefixSums)
    
    def _pathSum(self, root, currSum, targetSum, prefixSums):
        if not root:
            return 0
        
        ans = 0

        currSum += root.val
        if currSum == targetSum:
            ans = 1
            
        ans += prefixSums.get(currSum - targetSum, 0)

        prefixSums[currSum] = prefixSums.get(currSum, 0) + 1

        ans += self._pathSum(root.left, currSum, targetSum, prefixSums)
        ans += self._pathSum(root.right, currSum, targetSum, prefixSums)

        prefixSums[currSum] -= 1

        return ans


        
root = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11)))
sol = Solution()
print(sol.pathSum(root, 8))