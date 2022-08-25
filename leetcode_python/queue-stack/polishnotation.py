class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        ops = {"+", "-", "*", "/"}

        for el in tokens:
            if el in ops:
                opnd2 = int(stack[-1])
                stack.pop()
                opnd1 = int(stack[-1])
                stack.pop()

                res = self.evalExp(opnd1, opnd2, el)
                stack.append(str(res))

            else:
                stack.append(el)

        return stack[0]

    def evalExp(self, opnd1, opnd2, op):
        if op == "+":
            return opnd1 + opnd2
        elif op == "-":
            return opnd1 - opnd2
        elif op == "*":
            return opnd1 * opnd2
        elif op == "/": # need because python does Floor division
            if opnd1 < 0 and opnd2 < 0:
                return abs(opnd1)//abs(opnd2)
            elif opnd1 < 0 or opnd2 < 0:
                return -(abs(opnd1)//abs(opnd2))
            else:
                return opnd1//opnd2


solution = Solution()
print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))