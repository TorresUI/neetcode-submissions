class Solution:

    def encode(self, strs: List[str]) -> str:
        #Want to encode the string to contain Length of string + # that way the first element will be something like 5#Hello and that way we can solve that Hello is supposed to be the element decoded 
        res = ''
        for s in strs:
            lengthOfS = len(s)
            res += str(lengthOfS) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        l, r = 0, 0
        res = []
        while r < len(s):
            #first we want to increment r until we find the "#"
            while r < len(s) and s[r] != '#':
                r += 1
                        #We have now found the delimeter so from l to r is the length of the string
            lengthOfString = int(s[l:r])
            l = r + 1
            r += lengthOfString
            res.append(s[l: r + 1])

            r += 1
            l = r

        return res

            
