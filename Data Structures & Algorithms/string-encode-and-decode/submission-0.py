class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc += s + "-"
        return enc


    def decode(self, s: str) -> List[str]:
        dec = s.split("-")
        return dec[:-1]
        