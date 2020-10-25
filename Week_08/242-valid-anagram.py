class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        '''
        aset = set(s)
        for i in aset:
            if s.count(i) != t.count(i):
                return False
        return True
        
        count ={}
        for i in s:
            if i in count:
                count[i] +=1
            else:
                count[i] =1

        for j in t:
            if j in s:
                count[j] -=1
            else:
                return False

        for n in count:
            if count[n] !=0:
                return False
        return True
        '''
        s1 = {}
        s2 = {}
        for i in s:
            if i not in s1:
                s1[i]=1
            else:
                s1[i]+=1
        for j in t:
            if j not in s2:
                s2[j]=1
            else:
                s2[j]+=1

        # for i in s1:
        #     if i not in s2 or s1[i]!=s2[i]:
        #         return False
        # return True
        return s1 == s2