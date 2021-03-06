class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s:
            return True
        n = len(s)
        dic={}
        for i in range(n):
            if s[i] not in dic:
                if t[i] in dic.values():
                    return False
                else:
                    dic[s[i]]=t[i]
            else:
                if dic[s[i]]!=t[i]:
                    return False
        return True

