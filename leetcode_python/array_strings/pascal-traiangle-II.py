class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        current = [1]
        for i in range(1, rowIndex+1):
            temp = [1]

            length = len(current)
            index = 1
            while index < length:
                temp.append(current[index] + current[index-1])
                index += 1
            temp.append(1)

            current = temp

    
        return current

        
solution = Solution()
print(solution.getRow(1))