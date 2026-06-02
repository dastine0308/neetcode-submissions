class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        for char in s:
            if char in dic:
                top = stack.pop() if stack else '#'

                if top != dic[char]:
                    return False

            else:
                stack.append(char)

        return len(stack) == 0