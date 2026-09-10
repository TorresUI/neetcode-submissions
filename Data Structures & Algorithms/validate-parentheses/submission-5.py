class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        pstack = []
        


        for i in s: 
            if i in closeToOpen:
                if pstack and pstack[-1] == closeToOpen[i]:
                    pstack.pop()
                else:
                    return False
            else: 
                pstack.append(i)
        return len(pstack) == 0

                

        
