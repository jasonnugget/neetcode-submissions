import math
import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
        stack = []
        for i in tokens:
            if i in operations:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(math.trunc(operations[i](num1, num2)))
            
            else:
                stack.append(int(i))

        return stack[0]
