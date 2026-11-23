class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        def backtrack(i, currString):
            if i >= len(digits):
                res.append(currString)
                return
            
            nextLetters = digitToChar[digits[i]]

            for l in nextLetters:
                backtrack(i + 1, currString + l)
        
        backtrack(0, "")
        return [] if not digits else res