class Solution(object):
    def intersection(self, nums1, nums2):
        data = set()
        ans = []

        for num in nums1:
            if num not in data:
                data.add(num)

        for num in nums2:
            if num in data:
                ans.append(num)
                data.remove(num)

        return ans

solution = Solution()
print(solution.intersection([4,9,5], [9,4,9,8,4]))