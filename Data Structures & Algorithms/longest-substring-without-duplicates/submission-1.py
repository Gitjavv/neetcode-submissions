class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l = 0
        r = 1
        max_length = 1

        while r<len(s):
            if not s[r] in s[l:r]:
                r+=1
                max_length = max(r-l, max_length)
            else:
                l+=1
                r = l+1

        
        return max_length
        