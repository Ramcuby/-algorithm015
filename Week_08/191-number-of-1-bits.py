class Solution:
    def hammingWeight(self, n: int) -> int:
        # return bin(n).count('1')
        '''
        counter = 0
        while(n):
            n=n&(n-1)
            counter+=1
        return counter
        '''
        counter = 0
        s = bin(n)
        for i in range(len(s)):
            if s[i]=='1':
                counter+=1
        return counter