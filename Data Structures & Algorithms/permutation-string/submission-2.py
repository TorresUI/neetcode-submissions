class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        matches = 0
        s1Array = [0] * 26
        s2Array = [0] * 26

        if len(s2) < len(s1):
            return False

        for i in range(len(s1)):
            s1Array[ord(s1[i]) - ord('a')] += 1
            s2Array[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1Array[i] == s2Array[i]:
                matches += 1
        

        l, r = 0, len(s1)
        while r < len(s2):
            if matches == 26:
                return True
            
            #getting removed
            oldLeftLetter = ord(s2[l]) - ord('a')
            #getting added
            newRightLetter = ord(s2[r]) - ord('a')

            # Removing left character
            if s1Array[oldLeftLetter] == s2Array[oldLeftLetter]:  # was it a match before?
                matches -= 1                                        # we're about to break it
            s2Array[oldLeftLetter] -= 1
            if s1Array[oldLeftLetter] == s2Array[oldLeftLetter]:  # is it a match now?
                matches += 1                                        # we just fixed it

            # Adding right character
            if s1Array[newRightLetter] == s2Array[newRightLetter]:  # was it a match before?
                matches -= 1
            s2Array[newRightLetter] += 1
            if s1Array[newRightLetter] == s2Array[newRightLetter]:  # is it a match now?
                matches += 1            
            r += 1
            l += 1
        return matches == 26