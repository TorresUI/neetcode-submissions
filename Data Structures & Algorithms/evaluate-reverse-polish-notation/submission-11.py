class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:

            if i == "+":
                num1, num2 = int(stack.pop()), int(stack.pop())
                summ = num1 + num2
                stack.append(summ)
            
            elif i == "-":
                num1, num2 = int(stack.pop()), int(stack.pop())
                diff = num2 - num1
                stack.append(diff)


            elif i == "*":
                num1, num2 = int(stack.pop()), int(stack.pop())
                prod = num1 * num2
                stack.append(prod)


            elif i == "/":
                num1, num2 = int(stack.pop()), int(stack.pop())
                div = num2 / num1
                stack.append(int(div))

            else:
                stack.append(int(i))
        return stack[0]

