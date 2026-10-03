class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Sliding window approach with a fixed size.
        #check if the window contains the same letters if it does then return true otherwise return false

        if len(s2) < len(s1):
            return False

        currentWindowArray = [0] * 26
        targetSubString = [0] * 26

        matches = 0
        #Pre compute the arrays for the first window
        for i in range(len(s1)):
            currentWindowArray[ord(s2[i]) - ord('a')] += 1 
            targetSubString[ord(s1[i]) - ord('a')] += 1 


        #compute our current matches
        for i in range(len(currentWindowArray)):
            if currentWindowArray[i] == targetSubString[i]:
                matches += 1
        if matches == 26:
            return True
        #now we have our first substrings set and the matches. We need to iterate through the original s2 string to see if our matches ever hits 26 and then we know we have a permutation.
        l = 0
        r = len(s1)
        while r < len(s2):

            rIndex = ord(s2[r]) - ord('a')
            rPrevMatch = currentWindowArray[rIndex] == targetSubString[rIndex]
            currentWindowArray[rIndex] += 1

            

            if rPrevMatch:
                #Since it previously matched and we just changed the value it no longer matches
                matches -= 1
            elif not rPrevMatch and currentWindowArray[rIndex] == targetSubString[rIndex]:
                matches += 1

            
            #Now we have to do the same operation on the left.
            leftIndex = ord(s2[l]) - ord('a')
            isLeftMatchPrev = currentWindowArray[leftIndex] == targetSubString[leftIndex]
            currentWindowArray[leftIndex] -= 1

            if isLeftMatchPrev:
                #We previously had a match now we are removing it
                matches -= 1
            elif not isLeftMatchPrev and currentWindowArray[leftIndex] == targetSubString[leftIndex]:
                matches += 1
            
            if matches == 26:
                return True
            

            r += 1
            l += 1
        return False
        
                


