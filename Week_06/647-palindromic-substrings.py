class Solution:
    def countSubstrings(self, s: str) -> int:
        ''' #中心扩展
        n = len(s)
        ans = 0
        for i in range(2*n-1):
            left = int(i/2)
            right = int(i/2)+i%2
            while(left>=0 and right<n and s[left]==s[right]):
                left-=1
                right+=1
                ans+=1
        return ans
        '''
        count = 0
        dp = [[0]*len(s) for _ in range(len(s))]
        for j in range(len(s)):
            for i in range(j+1):
                if i == j:          #单个字母为回文
                    dp[i][j]=1
                    count += 1
                elif j-i==1 and s[i]==s[j]:   #相邻两个相同字母为回文
                    dp[i][j]=1
                    count += 1 
                elif j-i>1 and s[i]==s[j] and dp[i+1][j-1]:  #两个相同字母，且中间也为回文
                    dp[i][j] = 1
                    count += 1
        return count