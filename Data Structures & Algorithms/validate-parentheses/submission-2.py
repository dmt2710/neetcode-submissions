class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i, char in enumerate(s):
            if char == "[" or char == "(" or char == "{":
                stack.append(char)
            else:
                if not stack:
                    return False
                preChar = stack[-1]
                if preChar == "[" and char != "]":
                    return False
                elif preChar == "{" and char != "}":
                    return False
                elif preChar == "(" and char != ")":
                    return False
                stack.pop()

        return not stack