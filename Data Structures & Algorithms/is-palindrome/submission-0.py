class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        for char in s.lower():
            if char.isalnum():
                ss = ss + char
        n = len(ss) // 2
        for i in range(n):
            if ss[i] != ss[-1-i]: return False
        
        return True
