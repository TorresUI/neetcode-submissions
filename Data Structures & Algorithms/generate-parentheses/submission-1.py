class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtracking(numOfOpen, numOfClosed):
            if numOfOpen == numOfClosed == n:
                res.append("".join(stack))
                return
            
            if numOfOpen < n:
                stack.append("(")
                backtracking(numOfOpen + 1, numOfClosed)
                stack.pop()
                
            if numOfClosed < numOfOpen:
                stack.append(")")
                backtracking(numOfOpen, numOfClosed + 1)
                stack.pop()
        
        backtracking(0,0)
        return res