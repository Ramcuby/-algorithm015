class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        dp = [0]*n
        if n <=2 :return n
        dp[0],dp[1]=1,2
        for i in range(2,n):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n-1]
        '''
        if n<=2:return n
        f1,f2,f3 = 1,2,3
        for i in range(3,n+1):
            f3 = f1 + f2
            f1,f2 = f2,f3
        return f3