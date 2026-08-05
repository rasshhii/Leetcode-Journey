from collections import deque, defaultdict
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in invocations:
            graph[u].append(v)
            
        # BFS / DFS to find all suspicious methods reachable from k
        suspicious = set([k])
        queue = deque([k])
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
        # Check if any non-suspicious method invokes a suspicious method
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                # Cannot remove suspicious methods, return all methods
                return list(range(n))
                
        # Remove suspicious methods
        return [i for i in range(n) if i not in suspicious]