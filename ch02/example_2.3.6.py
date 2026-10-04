# Example 2.3.6 (Figure 2.3): Probability that at least two people in a group of $N$ share a birthday
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

N = np.arange(1, 61)
# nobody shares: (365/365)(364/365)...((365-N+1)/365)
p_none = np.cumprod((365 - N + 1) / 365)
p = 1 - p_none

n50 = N[p >= 0.5][0]
print(f"P(A) > 0.5 from N = {n50}: P(A) = {p[n50 - 1]:.3f}")

fig, ax = plt.subplots()
ax.plot(N, p, ".", color=col.pdf)
ax.axhline(0.5, **thr)
ax.axvline(n50, **thr)
ax.set_xlabel("$N$")
ax.set_ylabel("$P(A)$")

plt.show()
