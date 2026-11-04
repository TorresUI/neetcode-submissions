class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []

        for i in s:
            if i not in closeToOpen:
                #i is an open
                stack.append(i)
            else:
                if not stack or closeToOpen[i] != stack.pop():
                    return False
        return True if len(stack) == 0 else False