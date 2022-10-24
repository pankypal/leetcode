class Solution(object):
    def permute(self, str):
        self._permute(str, 0)

    def _permute(self, str, index):
        if index == len(str):
            print(''.join(str))
            return

        for i in range(index, len(str)):
            str[i], str[index] = str[index], str[i]
            self._permute(str, i+1)
            str[i], str[index] = str[index], str[i]

    def permute2(self, str):
        self._permute2(str, "")

    def _permute2(self, str, prefix):
        if len(str) == 0:
            print(''.join(prefix))
            return

        for i in range(0, len(str)):
            ch = str[i]
            newString = str[:i] + str[i+1:]
            self._permute2(newString, prefix+ch)


solution = Solution()
solution.permute(["a", "b", "c", "d"])
print("-------------")
solution.permute2(["a", "b", "c", "d"])