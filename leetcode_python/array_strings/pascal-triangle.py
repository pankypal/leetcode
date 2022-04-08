class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        result = []

        current = [1]
        result.append(current)
        for i in range(2, numRows+1):
            temp = [1]

            length = len(current)
            index = 1
            while index < length:
                temp.append(current[index] + current[index-1])
                index += 1
            temp.append(1)

            current = temp
            result.append(current)

    
        return result

        
solution = Solution()
print(solution.generate(5))