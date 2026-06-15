class Solution:
    def isValid(self, s: str) -> bool:
        opening_closing = {"(": ")","[":"]", "{":"}", None: None}
        current = []

        for char in s:
            if char in opening_closing:
                current.append(char)
                continue
            
            if len(current) > 0:
                inner = current[-1]
            else:
                inner = None

            if opening_closing[inner] == char:
                current.pop()
            else:
                return False
        
        if len(current) == 0:
            return True
        else:
            return False

        