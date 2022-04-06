class Solution(object):
    def merge(self, nums1, m, nums2, n):
        it = m + n - 1
        
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[it] = nums1[m-1]
                m -= 1
            else:
                nums1[it] = nums2[n-1]
                n -= 1
            it -= 1

        while m > 0:
            nums1[it] = nums1[m-1]
            m -= 1
            it -= 1

        while n > 0:
            nums1[it] = nums2[n-1]
            n -= 1
            it -= 1
        
        print(nums1)


solution = Solution()
solution.merge([5, 0], 1, [3], 1)