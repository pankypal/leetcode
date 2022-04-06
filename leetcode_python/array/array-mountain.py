class Solution(object):
    def validMountainArray(self, arr):
        size = len(arr)

        if size < 3:
            return False

        validate_inc = 0

        for i in range(1, size):
            if arr[i] == arr[i-1]:
                return False

            if arr[i] < arr[i-1]:
                break;

            validate_inc += 1

        if validate_inc == 0:
            return False

        validate_dec = 0

        y = 0
        for y in range(validate_inc+1, size):
            if arr[y-1] > arr[y]:
                validate_dec += 1
        
        if validate_dec != 0 and validate_inc + validate_dec == size-1:
            return True

        return False

    


solution = Solution()
print(solution.validMountainArray([0,1,2,1,2]))