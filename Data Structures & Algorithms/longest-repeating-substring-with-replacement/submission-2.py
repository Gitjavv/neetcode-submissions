from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0: return 0
        l = 0
        counter = defaultdict(int)
        max_length = 0
        maxf = 0

        for r in range(len(s)):
            counter[s[r]]+=1
            maxf = max(maxf, counter[s[r]])
            while r-l+1-maxf > k:
                counter[s[l]]-=1
                l+=1
            
            max_length = max(r-l+1, max_length)



        return max_length
