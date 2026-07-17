# 2215. Find the Difference of Two Arrays

# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where: 

# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.


class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        set1 = set(nums1)
        set2 = set(nums2)
        
        ans = []

        ans.append([])
        ans.append([])
        for el in set1:
            if el not in set2:
                ans[0].append(el)

        for el in set2:
            if el not in set1:
                ans[1].append(el)



        return ans


sol = Solution()
print(sol.findDifference([1,2,3], [2,4,6]))