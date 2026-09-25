class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            sLength = len(s)
            newString = str(sLength) + ';' + s
            res += newString
        return res
    def decode(self, s: str) -> List[str]:
        l = 0
        res = []
        while l < len(s):
            r = l + 1
            while s[r] != ';':
                r += 1
            
            length = int(s[l:r])
            res.append(s[r + 1 : r + 1 + length])
            l = r + 1 + length
        return res
