# Example 6.2.5 (Figure 6.6): Earliest and latest photon arrival times in a sample of 1000, with their sample correlation
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

n = 1000
U1 = rng.uniform(0, 1, size=n)
U2 = rng.uniform(0, 1, size=n)
T1 = np.minimum(U1, U2)
T2 = np.maximum(U1, U2)
r = np.corrcoef(T1, T2)[0, 1]

fig, ax = plt.subplots()
ax.plot(T1, T2, "o", color=col.emp, ms=2, alpha=0.6)
ax.plot([0, 1], [0, 1], **ref)
ax.set_xlabel("$T_1$ (earliest arrival)")
ax.set_ylabel("$T_2$ (latest arrival)")
ax.set_title(f"$r={r:.2f}$")

plt.show()
