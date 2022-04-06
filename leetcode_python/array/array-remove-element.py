from tabnanny import check


class Solution(object):
    def removeElement(self, nums, val):
        insert_pos = 0
        check_pos = 0

        while check_pos < len(nums):
            if nums[check_pos] != val:
                nums[insert_pos] = nums[check_pos]
                insert_pos += 1
            
            check_pos += 1

        print(nums)
        return insert_pos

solution = Solution()
print(solution.removeElement([0,1,2,2,3,0,4,2], 2))