# 1493. Longest Subarray of 1's After Deleting One Element

# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        max_len = 0
        zeroes = 0

        for right in range(len(nums)):
            zeroes += nums[right] == 0

            while zeroes > 1:
                zeroes -= nums[left] == 0
                left += 1

            max_len = max(max_len, right - left + 1  - zeroes)

        return max_len - 1 if zeroes == 0 else max_len
        

sol = Solution()
# print(sol.longestSubarray([0,1,1,1,0,1,1,0,1]))
# print(sol.longestSubarray([1,1,0,1]))
# print(sol.longestSubarray([1]))
# print(sol.longestSubarray([0]))
print(sol.longestSubarray([1,1,1]))