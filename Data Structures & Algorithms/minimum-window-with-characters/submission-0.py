class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s): return ""
        minf = float('inf')
        minsubstr = ""
        l = 0
        tCounter = defaultdict(int)
        sCounter = defaultdict(int)
        for char in t:
            tCounter[char] += 1

        for r in range(len(s)):
            sCounter[s[r]] += 1
            while all(sCounter[x]>=tCounter[x] for x in tCounter.keys()):
                if r-l+1<minf:
                     minf=r-l+1
                     minsubstr=s[l:r+1]
                sCounter[s[l]]-=1
                l+=1
        
        return minsubstr

        
        