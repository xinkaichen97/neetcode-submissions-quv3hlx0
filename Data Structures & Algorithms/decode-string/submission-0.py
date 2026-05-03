class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "]":
                # get string in brackets
                cur = []
                while stack[-1] != "[":
                    cur.append(stack.pop())
                stack.pop()

                # get digits
                digits = []
                while stack and stack[-1].isdigit():
                    digits.append(stack.pop())
                k = int("".join(reversed(digits)))

                # multiply
                stack.append("".join(reversed(cur)) * k)
            else:
                stack.append(c)
        
        return "".join(stack)
