# 1732. Find the Highest Altitude

# There is a biker going on a road trip. The road trip consists of n + 1 points at various altitudes. 
# The biker starts his trip on point 0 with altitude equal 0.
# You are given an integer array gain of length n where gain[i] is the net gain in altitude between 
# points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        if not gain:
            return 0
        
        max_el = 0
        curr_el = 0
        
        for el in gain:
            curr_el += el
            
            max_el = max(max_el, curr_el)

        return max_el



sol = Solution()
print(sol.largestAltitude([-4,-3,-2,-1,4,3,2]))
print(sol.largestAltitude([-5,1,5,0,-7]))