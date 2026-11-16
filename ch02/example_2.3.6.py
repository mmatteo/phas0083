# Example 2.3.6 (Figure 2.3): Probability that at least two people in a group of $N$ share a birthday
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

c = 0.5
N = np.arange(1, 61)
# nobody shares: (365/365)(364/365)...((365-N+1)/365)
p_none = np.cumprod((365 - N + 1) / 365)
p = 1 - p_none

N_c = N[p >= c][0]
print(f"P(A) >= {c} from N = {N_c}")
print(f"P(A) = {p[p >= c][0]:.3f} at N = {N_c}")

fig, ax = plt.subplots()
ax.plot(N, p, ".", color=col.pmf)
ax.axhline(c, color=col.ref, ls=":")
ax.axvline(N_c, color=col.ref, ls=":")
ax.set(xlabel="$N$", ylabel="$P(A)$")

plt.show()
