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
            
        


solution = Solution()
print(solution.generate([1,2,3]))
print(solution.generate_binary([1,2,3]))