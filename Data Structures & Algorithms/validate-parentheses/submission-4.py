class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashCloseToOpen = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if c in hashCloseToOpen:
                if stack and stack[-1] == hashCloseToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack and True