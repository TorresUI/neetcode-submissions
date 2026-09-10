class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        pstack = []
        


        for i in s: 
            if i not in closeToOpen:
                pstack.append(i)
            elif pstack and closeToOpen[i] == pstack[-1]:
                pstack.pop()
            else:
                return False
        return len(pstack) == 0

                

        
