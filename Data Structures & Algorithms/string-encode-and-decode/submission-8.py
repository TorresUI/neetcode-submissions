class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            length = len(i)
            res += str(length) + ';' + i
        return res
    def decode(self, s: str) -> List[str]:
        l, r = 0, 0
        res = []

        while r < len(s):
            while s[r] != ';':
                r += 1
            #We have found the delimeter.
            num = int(s[l:r])
            res.append(s[r + 1 : r + num + 1])
            l += (r - l) + num + 1 
            r += num + 1
        return res
