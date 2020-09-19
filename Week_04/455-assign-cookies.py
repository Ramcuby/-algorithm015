class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if g == [] or s == []: return 0
        g.sort(reverse=True)
        s.sort(reverse=True)
        i,j,count = 0,0,0
        while i != len(g) and j != len(s):
            if g[i] <= s[j]:
                j += 1
                count += 1
            i += 1
        return count