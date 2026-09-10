class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l].lower() == s[r].lower() and self.alphaNum(s[l]) and self.alphaNum(s[r]):
                l += 1
                r -= 1
            elif not self.alphaNum(s[l]):
                l += 1
                continue
            elif not self.alphaNum(s[r]):
                r -=1
            else:
                print(l,r)
                return False

        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

