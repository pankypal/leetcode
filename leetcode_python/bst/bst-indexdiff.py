from sortedcontainers import SortedList

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        slist = SortedList()

        for i in range(len(nums)):
            if i > indexDiff:
                slist.remove(nums[i-(indexDiff+1)])

            pos1 = slist.bisect_left(nums[i] - valueDiff)
            pos2 = slist.bisect_right(nums[i] + valueDiff)

            if pos1 != pos2:
                return True

            slist.add(nums[i])

        return False


solution = Solution()
print(solution.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))