import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

output_dir = os.path.expanduser("~/logs")
os.makedirs(output_dir, exist_ok=True)

fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
ax.axis('off')
plt.title("FIG. 4\nCARRIER-PAYLOAD DOCKING STATE", fontsize=14, fontweight='bold', pad=20)

# Outer Carrier - Dashed Circle
ax.add_patch(patches.Circle((0.5, 0.5), 0.3, fill=False, lw=2, ls='--'))

# Inner Payload - Fixed Syntax for RegularPolygon
# We pass the center as a single tuple to 'xy' explicitly
poly = patches.RegularPolygon(xy=(0.5, 0.5), numVertices=6, radius=0.1, fill=False, lw=2, hatch='//')
ax.add_patch(poly)

ax.text(0.5, 0.85, "Acoustic Carrier", ha='center', fontweight='bold')
ax.text(0.5, 0.5, "CLR01", ha='center', va='center', fontweight='bold')
ax.annotate('Ejection (1,450 m/s)', xy=(0.85, 0.5), xytext=(0.6, 0.5), 
             arrowprops=dict(arrowstyle='->', lw=2), fontweight='bold')

plt.savefig(os.path.join(output_dir, "FIG_4_Molecular.png"), bbox_inches='tight')
print("--- FIG_4_Molecular.png GENERATED SUCCESSFULLY ---")
