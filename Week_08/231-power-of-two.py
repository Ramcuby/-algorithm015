class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''
        if n == 0:
            return False
        return n & (-n) == n
        '''
        # if n <= 0:return False
        if n>0:
            return (n&n-1)==0
        else:
            return False 
        '''
        if n <= 0:return False
        while(n%2==0):
            n=n/2
        if n ==1 : return True
        else:
            return False
        # 4
        if n>0:
            return bin(n).count('1')==1
        else:
            return False
        '''