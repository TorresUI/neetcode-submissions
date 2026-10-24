class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def isPalindrome(string):
            l, r = 0, len(string) - 1
            while l <= r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True
        def dfs(i):
            if i >= len(s):
                res.append(curr.copy())
                return
            
            #otherwise we need to check all substrings within the subArray starting at i 
            j = i
            while j < len(s):
                print("hello", s[i:j+1])
                #check if the substring s[j + 1] is a palindrome if it is add it to the current list, iterate i and then do backtrack on the remaining substring
                if isPalindrome(s[i:j + 1]):
                    #its a palindrome add it to the stack
                    curr.append(s[i: j + 1])
                    dfs(j + 1)
                    curr.pop()
                j += 1
            
        dfs(0)
        return res