class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        #iterate through a window at each step checking if char frequencies are the same as for s1. Window size should be fixed length of s1

        alphaS1 = [0] * 26

        for i in s1:
            alphaS1[ord(i) - ord('a')] += 1

        
        l, r = 0, len(s1) - 1
        matches = 26

        alphaS2 = [0] * 26 

        for i in s2[l:r+1]:
            alphaS2[ord(i) - ord('a')] += 1
    

        #check how many matches there are for the intial window
        for i in range(len(alphaS1)):
            if alphaS1[i] != alphaS2[i]:
                #there is a mismatch
                matches -= 1
        
        #Now we iterate the window through S2 and see if at any point the letter frequencies match to get 26 total matches.

        while r < len(s2) - 1:

            if matches == 26:
                return True

            #increment right pointer
            r += 1
            newLetter = s2[r]
            newLetterIndex = ord(newLetter) - ord('a')
            isRightMatchBefore = alphaS1[newLetterIndex] == alphaS2[newLetterIndex]
            alphaS2[newLetterIndex] += 1

            
            if isRightMatchBefore:
                #We are going to add to r in AlphaS2 so now it will no longer be matching
                matches -= 1
            else:
                #they were not matching before lets check if they match now after adding. 
                
                if alphaS2[newLetterIndex] == alphaS1[newLetterIndex]:
                    matches += 1
            
            #Now we need to move up the left pointer.

            #first decrement the old left pointer and check if theres a new match
            oldLetter = s2[l]
            oldLetterIndex = ord(oldLetter) - ord('a')
            isOldLeftMatching = alphaS2[oldLetterIndex] == alphaS1[oldLetterIndex]
            alphaS2[oldLetterIndex] -= 1
            if isOldLeftMatching:
                #not going to be matching anymore
                matches -= 1
            else:
                if alphaS2[oldLetterIndex] == alphaS1[oldLetterIndex]:
                    matches += 1
            l += 1
        return matches == 26