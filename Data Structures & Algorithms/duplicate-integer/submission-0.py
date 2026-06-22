class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countDict = {}
        for num in nums :
            if num in countDict:
                return True
            countDict[num] = 1
        return False