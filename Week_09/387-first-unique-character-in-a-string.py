class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        temp = {}
        for i in s:
            if i not in temp:
                temp[i]=1
            else:
                temp[i]+=1
        for i in range(len(s)):
            if temp[s[i]]==1:
                return i
        return -1