from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        s1_counter = defaultdict(int)
        for char in s1:
            s1_counter[char]+=1

        s1_len = len(s1)
        s2_counter = defaultdict(int)
        for j in range(s1_len):
            s2_counter[s2[j]]+=1
        
        if s2_counter == s1_counter: return True
        
        for r in range(len(s2)-s1_len):
            s2_counter[s2[r]]-=1
            if s2_counter[s2[r]] == 0: del s2_counter[s2[r]]
            s2_counter[s2[r+s1_len]] += 1
            if s2_counter == s1_counter: return True
        
        return False


