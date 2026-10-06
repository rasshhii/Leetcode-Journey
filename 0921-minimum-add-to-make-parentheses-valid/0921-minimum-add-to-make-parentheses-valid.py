class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_c = close_c = 0

        for char in s:
            if char == "(":
                open_c += 1
            elif open_c > 0:
                open_c -= 1
            else:
                close_c += 1

        return open_c + close_c