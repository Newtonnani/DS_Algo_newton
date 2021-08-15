class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''.join(e for e in s if e.isalnum()).lower()
        return res == res[::-1]
        
