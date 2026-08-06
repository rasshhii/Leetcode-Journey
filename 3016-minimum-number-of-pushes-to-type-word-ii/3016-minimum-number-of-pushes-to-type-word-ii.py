from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        sorted_counts = sorted(freq.values(), reverse=True)
        
        total_pushes = 0
        for i, count in enumerate(sorted_counts):
            total_pushes += count * (i // 8 + 1)
            
        return total_pushes