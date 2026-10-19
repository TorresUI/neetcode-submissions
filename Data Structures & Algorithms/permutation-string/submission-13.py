class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Array = [0] * 26
        s2Array = [0] * 26

        if len(s2) < len(s1):
            return False

        for i in range(len(s1)):
            s1Array[ord(s1[i]) - ord('a')] += 1
            s2Array[ord(s2[i]) - ord('a')] += 1
                
        #We have now built the arrays that contain the letters and their frequency

        #we want to compute how many matches we are at that way when we iterate through s2 we can see if we ever arrive to a point where both alphabet arrays are equal. if they are equal then we have visited a substring which is a permutation of s1.
        matches = 0
        for i in range(len(s2Array)):
            if s1Array[i] == s2Array[i]:
                matches += 1
        print(matches)
        if matches == 26:
            return True
        #s2Array is initialized to searched size s1. We need to sliding window this now until the end of s2. At each step check if matches is 26 that means the full arrays match and there is some permutation that matches.
        l, r = 0, len(s1)
        while r < len(s2):
            #We need to first check if left pointer matches and check if right pointer matches
            #then we need to decrement the freq of the letter that matches s2[l]. if it was matching before it is no longer matching so matches -= 1. If it was not matching before check if it is matching now.

            #We need to add s2[r] to the freq list. if it was matching before it is no longer matching. if it was not matching before check if it is matching now.
            rightLetter = s2[r]
            leftLetter = s2[l]
            rightIndex = ord(rightLetter) - ord('a')
            leftIndex = ord(leftLetter) - ord('a')

            rightMatching = s1Array[rightIndex] == s2Array[rightIndex]
            #Process right first
            s2Array[rightIndex] += 1
            if rightMatching:
                #Right was previously matching, we made a change it no longer matches
                matches -= 1
            else:
                matches += 1 if s1Array[rightIndex] == s2Array[rightIndex] else 0
            
            leftMatching = s1Array[leftIndex] == s2Array[leftIndex]
            s2Array[leftIndex] -= 1
            
            if leftMatching:
                matches -= 1
            else:
                matches += 1 if s1Array[leftIndex] == s2Array[leftIndex] else 0
            
            l += 1
            r += 1
            if matches == 26:
                return True
        return False

        
