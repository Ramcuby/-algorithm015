class Solution:
    def numDecodings(self, s: str) -> int:
        size = len(s)
        dp = [0]*size

        dp[0] = 1 if s[0]!='0' else 0
        if size >= 2:
            dp[1] = 1 if s[1] == '0' and 0<int(s[0])<=2 \
                    else 0 if s[1]=='0' \
                    else 2 if 10<int(s[0]+s[1])<=26 \
                    else dp[0]

        for i in range(2,size):
            dp[i] = dp[i-2] if s[i]=='0' and 0<int(s[i-1])<=2 \
                    else 0 if s[i]=='0' \
                    else dp[i-2]+dp[i-1] if 10<int(s[i-1]+s[i])<=26 \
                    else dp[i-1]
        # print(dp)
        return dp[-1]