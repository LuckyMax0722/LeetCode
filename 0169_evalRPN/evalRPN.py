class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []
        idx = 0

        symbol = ['+','-','*','/']

        while tokens:
            if tokens[0] not in symbol:
                stack.append(tokens[0])
                tokens.pop(0)
            else:
                out = 0
                if tokens[0] == '+':
                    out = int(stack[-2]) + int(stack[-1])
                elif tokens[0] == '-':
                    out = int(stack[-2]) - int(stack[-1])
                elif tokens[0] == '*':
                    out = int(stack[-2]) * int(stack[-1])
                elif tokens[0] == '/':
                    if int(stack[-2]) <= 0 and int(stack[-1]) > 0:
                        out = -int(stack[-2]) / int(stack[-1])
                        out = -out
                    elif int(stack[-2]) >= 0 and int(stack[-1]) < 0:
                        out = int(stack[-2]) / -int(stack[-1])
                        out = -out
                    else:
                        out = int(stack[-2]) / int(stack[-1])

                stack.pop()
                stack.pop()
                stack.append(str(out))
                tokens.pop(0)

        return int(stack[0])