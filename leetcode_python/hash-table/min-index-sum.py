class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        mapping = dict()

        for i, item in enumerate(list1):
            mapping[item] = i

        minVal = float("inf")
        res = []
        for i, item in enumerate(list2):
            if item in mapping:
                sum = mapping[item] + i
                if sum < minVal:
                    minVal = sum
                    res= []
                    res.append(item)
                elif sum == minVal:
                    res.append(item)

        return res
        

solution = Solution()
print(solution.findRestaurant(
    ["Shogun","Tapioca Express","Burger King","KFC"],
    ["KFC","Shogun","Burger King"]))