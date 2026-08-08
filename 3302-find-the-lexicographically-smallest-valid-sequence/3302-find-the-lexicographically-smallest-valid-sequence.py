class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)
        last = [-1] * m
        p2 = m - 1
        
        for i in range(n - 1, -1, -1):
            if p2 >= 0 and word1[i] == word2[p2]:
                last[p2] = i
                p2 -= 1

        ans = []
        i = 0
        changed = False

        for j in range(m):
            while i < n:
                if word1[i] == word2[j]:
                    if j == m - 1 or last[j + 1] > i or not changed:
                        ans.append(i)
                        i += 1
                        break
                else:
                    if not changed and (j == m - 1 or last[j + 1] > i):
                        ans.append(i)
                        changed = True
                        i += 1
                        break
                i += 1

        return ans if len(ans) == m else []