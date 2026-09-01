from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        start_x, start_y = -1, -1
        litters = []
        
       
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_x, start_y = r, c
                elif classroom[r][c] == 'L':
                    litters.append((r, c))
        
        total_litters = len(litters)
        if total_litters == 0:
            return 0
        
        full_mask = (1 << total_litters) - 1
        
        
        litter_map = {pos: i for i, pos in enumerate(litters)}
        
        
        best_energy = {}
        
        queue = deque([(start_x, start_y, 0, energy, 0)])  
        best_energy[(start_x, start_y, 0)] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        
        while queue:
            x, y, mask, e, steps = queue.popleft()
            
            if mask == full_mask:
                return steps
            
            
            if e == 0:
                continue
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                
                if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != 'X':
                    ne = e - 1  
                    nmask = mask
                    
                    cell = classroom[nx][ny]
                    
                    
                    if cell == 'L':
                        litter_idx = litter_map[(nx, ny)]
                        nmask |= (1 << litter_idx)
                    
                   
                    if cell == 'R':
                        ne = energy
                    
                    
                    if ne > best_energy.get((nx, ny, nmask), -1):
                        best_energy[(nx, ny, nmask)] = ne
                        queue.append((nx, ny, nmask, ne, steps + 1))
        
        return -1