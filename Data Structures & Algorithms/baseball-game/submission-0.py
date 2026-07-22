class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            value = operations[i]
            if value.replace('-', '').isnumeric():
                stack.append(int(value))
            elif value == "+":
                stack.append(stack[-1] + stack[-2])
            elif value == "D":
                stack.append(stack[-1] * 2)
            elif value == "C":
                stack.pop()
        
        return sum(stack)