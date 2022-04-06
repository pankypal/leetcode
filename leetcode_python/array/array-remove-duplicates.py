from tabnanny import check

from pyparsing import nums


class Solution(object):
    def removeDuplicates(self, nums):
        size = len(nums)

        if size <= 1:
            return size

        check_pos = 1
        insert_pos = 0
        while check_pos < size:
            if nums[insert_pos] != nums[check_pos]:
                insert_pos += 1
                nums[insert_pos] = nums[check_pos]
            
            check_pos += 1

        print(nums)
        return insert_pos+1
        

solution = Solution()
print(solution.removeDuplicates([1,2,2,3,3,3,3,4]))