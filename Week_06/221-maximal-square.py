class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not len(matrix):
            return 0

        maxarea = 0
        m,n = len(matrix),len(matrix[0])  # m为行，n为列
        dp = [[0]*n for _ in range(m)]    # 初始化，先列后行 
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    if i==0 or j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    maxarea=max(maxarea,dp[i][j])
        
        return maxarea*maxarea