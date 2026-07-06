class Solution(object):
    def generate(self, nums):
        if not nums:
            return []
            
        res = [[]]

        for i in nums:
            curr = []
            for el in res:
                curr.append(el + [i])
            
            res.extend(curr)

        return res

    def generate_binary(self, nums):
        n = len(nums)
        N = 2**n

        res = []
        for i in range(N):
            curr = []
            for j in range(n):
                if (i >> j) % 2 == 1:
                    curr.append(nums[j])

            res.append(curr)

        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible subsets of the given array.
      
        Args:
            nums: List of integers
          
        Returns:
            List of all possible subsets
        """
      
        def backtrack(index: int) -> None:
            """
            Recursive helper function to generate subsets using backtracking.
          
            Args:
                index: Current index in the nums array
            """
            # Base case: reached the end of the array
            if index == len(nums):
                # Add a copy of current subset to the result
                result.append(current_subset[:])
                return
          
            # Choice 1: Exclude the current element
            backtrack(index + 1)
          
            # Choice 2: Include the current element
            current_subset.append(nums[index])
            backtrack(index + 1)
          
            # Backtrack: remove the element we just added
            current_subset.pop()
            
        


solution = Solution()
print(solution.generate([1,2,3]))
print(solution.generate_binary([1,2,3]))