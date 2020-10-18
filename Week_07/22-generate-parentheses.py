class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def gen(left,right,s):
            if(left==n and right==n):
                res.append(s)
                return res
            if(left<n):
                s+='('
                gen(left+1,right,s)
                s=s[:-1]
            if(right<left):
                s+=')'
                gen(left,right+1,s)
                s=s[:-1]
        gen(0,0,'')
        return res