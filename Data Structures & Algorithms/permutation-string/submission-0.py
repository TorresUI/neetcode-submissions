class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        for c in s1:
            need[c] = need.get(c, 0) + 1

        window = {}
        for c in s2[:len(s1)]:
            window[c] = window.get(c, 0) + 1

        if window == need:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1

            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            l += 1

            if window == need:
                return True

        return False