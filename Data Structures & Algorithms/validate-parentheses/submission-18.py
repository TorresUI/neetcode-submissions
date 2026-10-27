class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []

        for i in s:
            if i not in closeToOpen:
                #open parantheses we need to add to the stack
                stack.append(i)
            
            else:
                #close parentheses
                latestOpenParentheses = stack.pop() if stack else None
                if closeToOpen[i] != latestOpenParentheses:
                    return False
        
        return True if not stack else False
