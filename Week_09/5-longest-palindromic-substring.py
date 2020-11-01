class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        '''
        n =len(s)
        res = ""
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                dp[i][j]=s[i]==s[j] and (j-i<2 or dp[i+1][j-1])
                if dp[i][j] and j-i+1>len(res):
                    res = s[i:j+1]
        return res
        '''

        n = len(s)
        temp = []
        for i in range(n):
            if i+1<n and s[i+1]==s[i]:
                p,q=i,i+1
                while(p-1>=0 and q+1<n and s[p-1]==s[q+1]):
                        p-=1
                        q+=1
                temp.append(s[p:q+1])
            if i-1>=0 and i+1<n and s[i+1]==s[i-1]:
                p,q=i-1,i+1
                while(p-1>=0 and q+1<n and s[p-1]==s[q+1]):
                        p-=1
                        q+=1
                temp.append(s[p:q+1])
            else:
                temp.append(s[i])
        return max(temp,key=len)