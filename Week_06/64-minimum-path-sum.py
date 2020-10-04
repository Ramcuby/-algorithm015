class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        sum = [[0 for _ in range(n)] for _ in range(m)]
        sum[0][0] = grid[0][0]
        #  初始化
        for i in range(1,m):
            sum[i][0]=sum[i-1][0]+grid[i][0]
        for j in range(1,n):
            sum[0][j]=sum[0][j-1]+grid[0][j]
        # 动态规划
        for i in range(1,m):
            for j in range(1,n):
                sum[i][j]=min(sum[i-1][j]+grid[i][j],sum[i][j-1]+grid[i][j])
        return sum[m-1][n-1]