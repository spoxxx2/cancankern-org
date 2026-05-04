import json
import math
import os

class SovereignLatticeV29:
    def __init__(self):
        self.node = "Panama Lane Sovereign Node"
        self.tray_size = 10.16 # 4 inches in cm
        self.a = 1.5 # Lattice constant (cm)
        self.delta = 0.2 # Symmetry breaking shift (cm)

    def generate_pillars(self):
        pillars = []
        rows = 8
        cols = 8
        for r in range(rows):
            for c in range(cols):
                x_center = c * self.a * 1.5
                y_center = r * self.a * math.sqrt(3)
                if c % 2 == 1:
                    y_center += (self.a * math.sqrt(3)) / 2

                for i in range(6):
                    angle = math.radians(i * 60)
                    dist = self.a / math.sqrt(3)
                    if i % 2 == 0: 
                        dist -= self.delta
                    
                    px = x_center + dist * math.cos(angle)
                    py = y_center + dist * math.sin(angle)
                    
                    if 0 <= px <= self.tray_size and 0 <= py <= self.tray_size:
                        pillars.append({"x": round(px, 3), "y": round(py, 3)})
        return pillars

    def log_audit(self):
        coords = self.generate_pillars()
        audit = {
            "timestamp": "2026-03-27",
            "architect": "Casey Lee Canfield",
            "node": self.node,
            "pillar_count": len(coords),
            "coordinates": coords
        }
        
        # Save to your local gemini.md vault
        with open("gemini.md", "a") as f:
            f.write(f"\n### SOVEREIGN LATTICE AUDIT v29.0: {audit['timestamp']}\n")
            f.write(json.dumps(audit, indent=2))
            f.write("\n---\n")
        return len(coords)

if __name__ == "__main__":
    mapper = SovereignLatticeV29()
    count = mapper.log_audit()
    print(f"\n[SUCCESS] V29.0 Lattice Map Generated.")
    print(f"[INFO] {count} pillars logged to gemini.md.")
    print(f"[ACTION] Ready for physical assembly at 1501 Pearl St.\n")
