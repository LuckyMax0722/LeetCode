class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        '''
        stack = []
        s = [char for char in s if char != ' ']

        count = -1
        idx = 0

        while s:
            count = count + 1
            if s[0] != ')':
                stack.append(s[0])
                s.pop(0)
            elif s[0] == '(':
                idx = count
            else:
                while True:
                    if count - idx == 2:
                        out = stack[-1]
                        stack.pop()
                        stack.pop()
                        stack.append(out)
                        if len(stack) == 1:
                            return int(stack[0])
                    else:
                        out = 0
                        if stack[-2] == '+':
                            out = int(stack[-3]) + int(stack[-1])
                        elif stack[-2] == '-':
                            out = int(stack[-3]) - int(stack[-1])
                        stack.pop()
                        stack.pop()
                        stack.pop()
                        if stack[-1] != '(':
                            stack.append(str(out))
                        else:
                            stack.pop()
                            stack.append(str(out))
                            break
                s.pop(0)

        if len(stack) == 1:
            return int(stack[0])
        else:
            while stack:
                out = 0
                if stack[1] == '+':
                    out = int(stack[0]) + int(stack[2])
                elif stack[1] == '-':
                    out = int(stack[0]) - int(stack[2])
                stack.pop(0)
                stack.pop(0)
                stack.pop(0)

                stack.insert(0, str(out))

                if len(stack) == 1:
                    return int(stack[0])
        # 做不出来 太难了
        '''

        ops = [1]
        sign = 1

        ret = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = ops[-1]
                i += 1
            elif s[i] == '-':
                sign = -ops[-1]
                i += 1
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                ret += num * sign
            print(ops, sign, ret)
        return ret
