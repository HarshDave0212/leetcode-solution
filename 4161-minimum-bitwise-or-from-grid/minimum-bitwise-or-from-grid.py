class Solution:
    def minimumOR(self, grid):
        ans = (1 << 20) - 1   # Initially all 20 bits set to 1
        
        for bit in range(19, -1, -1):   # From bit 19 down to 0
            wants = ans ^ (1 << bit)    # Try removing this bit
            pos = True
            
            for row in grid:
                sub = False
                for x in row:
                    if (wants | x) == wants:
                        sub = True
                        break
                if not sub:
                    pos = False
                    break
            
            if not pos:
                continue
            
            ans = wants
        
        return ans