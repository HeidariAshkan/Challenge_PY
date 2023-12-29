class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t : return True
        if len(s) != len(t): return False
        countS,countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i] , 0)
            countT[t[i]] = 1 + countT.get(t[i] , 0)
        return countT == countS    


#Anoter Way
# from collections import Counter


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return Counter(s) == Counter(t)

  
        