import math

class AsciiLatticeV29:
    def __init__(self):
        self.size = 20 # Map size for terminal display
        self.a = 3 # Scaling constant
        self.delta = 1 # Shift scaling for visibility

    def generate_ascii_map(self):
        # Create empty grid
        grid = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        
        for r in range(self.size):
            for c in range(self.size):
                if (r + c) % 2 == 0:
                    grid[r][c] = '.' # Aluminum background placeholder

        # Plot 4 test unit cells with broken symmetry
        # (Standard hex points are (0,0), shifted points use delta)
        points = [
            (0, 0), (self.a, 0), (0, self.a), (self.a, self.a), # Standard
            (self.a/2 + self.delta, self.a/2), (self.a/2, self.a/2 + self.delta) # Shifted
        ]
        
        origin_x = 5
        origin_y = 5

        for px, py in points:
            x = origin_x + int(px)
            y = origin_y + int(py)
            if 0 <= x < self.size and 0 <= y < self.size:
                if (px + py) % (self.a * 1.5) < 1:
                    grid[x][y] = '#' # Standard Pillar
                else:
                    grid[x][y] = '*' # *Asymmetric Shifted Pillar*
                    
        # Print Grid
        print("\n[--- 4 INCH SUBSTRATE ---]\n")
        for row in grid:
            print(" ".join(row))
        print("\n[--- 4 INCH SUBSTRATE ---]\n")
        print("Key:\n. = Aluminum\n# = Standard Pillar\n* = Asymmetric Shifted Pillar\n")

if __name__ == "__main__":
    mapper = AsciiLatticeV29()
    mapper.generate_ascii_map()
