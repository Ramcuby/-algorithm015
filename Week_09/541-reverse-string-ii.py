class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
        n =len(s)
        s[0:k]=s[k-1::-1]
        p,q=2*k,k-1+2*k
        while(p<n):
            s[p:q+1]=s[q:p-1:-1]
            p+=k*2
            q=q+k*2 if q+2*k<n else n-1
        return ''.join(s)
