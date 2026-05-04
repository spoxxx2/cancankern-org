import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

output_dir = os.path.expanduser("~/logs")
os.makedirs(output_dir, exist_ok=True)

def setup_uspto_figure(fig_num, title):
    fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
    ax.axis('off')
    plt.title(f"FIG. {fig_num}\n{title}", fontsize=14, fontweight='bold', pad=20)
    return fig, ax

# Generate all 4 to be safe
# FIG 1
f1, a1 = setup_uspto_figure(1, "BIO-ACOUSTIC MANUFACTURING PIPELINE")
a1.add_patch(patches.Rectangle((0.2, 0.4), 0.6, 0.2, fill=False, lw=2))
a1.text(0.5, 0.5, "Input -> Synthesis -> Verification", ha='center', fontweight='bold')
f1.savefig(os.path.join(output_dir, "FIG_1_Pipeline.png"))

# FIG 2
f2, a2 = plt.subplots(figsize=(8, 6), dpi=300)
t = np.linspace(0, 0.05, 1000)
a2.plot(t, np.mod(t*650, 1), 'k--', label='650Hz Baseline')
a2.plot(t, np.mod(t*648.12, 1), 'k-', label='-1.88Hz Shift')
a2.set_title("FIG. 2: RESONANT DRAG")
a2.legend()
f2.savefig(os.path.join(output_dir, "FIG_2_Spectral.png"))

# FIG 3
f3, a3 = setup_uspto_figure(3, "SOVEREIGN MESH CONTROL UNIT")
a3.add_patch(patches.Rectangle((0.3, 0.4), 0.4, 0.2, fill=False, lw=2))
a3.text(0.5, 0.5, "Node 93307 Control", ha='center', fontweight='bold')
f3.savefig(os.path.join(output_dir, "FIG_3_BlockDiagram.png"))

# FIG 4 - FIXED SYNTAX
f4, a4 = setup_uspto_figure(4, "CARRIER-PAYLOAD DOCKING STATE")
a4.add_patch(patches.Circle((0.5, 0.5), 0.3, fill=False, lw=2, ls='--'))
# The fix: positional arguments only for RegularPolygon
poly = patches.RegularPolygon((0.5, 0.5), 6, 0.1, fill=False, lw=2, hatch='//')
a4.add_patch(poly)
a4.text(0.5, 0.85, "Acoustic Carrier", ha='center', fontweight='bold')
a4.annotate('Ejection (1,450 m/s)', xy=(0.85, 0.5), xytext=(0.6, 0.5), arrowprops=dict(arrowstyle='->', lw=2))
f4.savefig(os.path.join(output_dir, "FIG_4_Molecular.png"))

print("--- ALL 4 FIGURES GENERATED ---")
