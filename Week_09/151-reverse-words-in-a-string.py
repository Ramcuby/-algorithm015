class Solution:
    def reverseWords(self, s: str) -> str:
        strings = s.split()
        strings = strings[::-1]
        return ' '.join(strings)