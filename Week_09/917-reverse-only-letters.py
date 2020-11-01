class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S=list(S)
        n = len(S)
        i,j = 0,n-1
        while(i<j):
            if(S[i].isalpha() and S[j].isalpha()):
                S[i],S[j] = S[j],S[i]
                i+=1
                j-=1
            else:
                if not S[i].isalpha():
                    i+=1
                if not S[j].isalpha():
                    j-=1
        return ''.join(S)