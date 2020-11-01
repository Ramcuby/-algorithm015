class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        is_Palindrome = lambda s:s==s[::-1]
        
        if is_Palindrome(s):
            return True

        i,j = 0,len(s)-1
        while(i<j):
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return is_Palindrome(s[i+1:j+1]) or is_Palindrome(s[i:j])
        # return True