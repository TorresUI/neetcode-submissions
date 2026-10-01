class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []
        for i in s:
            if i in closeToOpen and stack:
                #we encountered a closing character
                if stack[-1] != closeToOpen[i]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0

