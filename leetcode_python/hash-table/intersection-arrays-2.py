class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counter = dict()

        for num in nums1:
            count = 0
            if num in counter:
                count = counter[num]

            count += 1
            counter[num] = count

        res = []
        for num in nums2:
            if num in counter:
                count = counter[num]
                count -= 1

                res.append(num)
                if count == 0:
                    del counter[num]
                else:
                    counter[num] = count

        return res

solution = Solution()
print(solution.intersect([4,9,5], [9,4,9,8,4]))