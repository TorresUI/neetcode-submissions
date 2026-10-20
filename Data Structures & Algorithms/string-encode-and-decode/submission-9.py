class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + '#' + i
        return res 
    def decode(self, s: str) -> List[str]:
        #We know the first(or few) chars are going to be the length of the string followed by the delimeter.
        l, r = 0, 0
        res = []

        while r < len(s):
            #First we want to increment R until it reaches the delimeter
            while s[r] != '#':
                r += 1
            #Now R is at the delimeter we know that between l and r is the length
            length = int(s[l:r])
            l = r + 1 #move left pointer up to the first letter in the word
            r = r + length + 1
            res.append(s[l:r])
            l = r

        return res