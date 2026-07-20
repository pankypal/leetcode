# 735. Asteroid Collision


# We are given an array asteroids of integers representing asteroids in a row. 
# The indices of the asteroid in the array represent their relative position in space.

# For each asteroid, the absolute value represents its size, and the sign represents its 
# direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode.
# If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        if not asteroids:
            return []
        
        st = []

        for el in asteroids:
            if not st:
                st.append(el)
            else:
                if el < 0:
                    should_insert = False
                    while st:
                        if st[-1] < 0:
                            should_insert = True
                            break
                        if abs(st[-1]) == abs(el):
                            st.pop()
                            should_insert = False
                            break
                        if abs(st[-1]) > abs(el):
                            should_insert = False
                            break
                        if abs(st[-1]) < abs(el):
                            st.pop()
                            should_insert = True
                    
                    if should_insert:
                        st.append(el)
                else:
                    st.append(el)

        return st

    def asteroidCollision1(self, asteroids):
        stack = []

        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:  # a < 0
                # Destroy the previous positive one(s).
                while stack and stack[-1] > 0 and stack[-1] < -a:
                    stack.pop()
                
                if not stack or stack[-1] < 0:
                    stack.append(a)
                elif stack[-1] == -a:
                    stack.pop()  # Both asteroids explode.
                else:  # stack[-1] > the current asteroid.
                    pass  # Destroy the current asteroid, so do nothing.

        return stack 

sol = Solution()
#print(sol.asteroidCollision([3,5,-6,2,-1,4]))
#print(sol.asteroidCollision([8,-8]))
#print(sol.asteroidCollision([10,2,-5]))
print(sol.asteroidCollision([-2,-1,1,2]))
