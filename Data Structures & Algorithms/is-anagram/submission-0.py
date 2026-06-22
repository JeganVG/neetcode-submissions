class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countADict = {}

        for c in s:
            countADict[c] = countADict.get(c, 0) + 1
        
        for c in t:
            if c not in countADict:
                return False
            
            countADict[c] -= 1

            if countADict[c] < 0:
                return False
            
        return True

        