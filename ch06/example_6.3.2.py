# Example 6.3.2 (Figure 6.8): Sample mean, variance and correlation of the arrival times on the first $m$ observations, with the population values
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

n = 10_000
U1 = rng.uniform(0, 1, size=n)
U2 = rng.uniform(0, 1, size=n)
T1 = np.minimum(U1, U2)
T2 = np.maximum(U1, U2)

# the statistics on the first m observations, m = 10, ..., n
m = np.arange(10, n + 1)
T1_bar = [T1[:i].mean() for i in m]
T2_bar = [T2[:i].mean() for i in m]
S2_T1 = [T1[:i].var(ddof=1) for i in m]
S2_T2 = [T2[:i].var(ddof=1) for i in m]
r = [np.corrcoef(T1[:i], T2[:i])[0, 1] for i in m]

limits = [1 / 3, 2 / 3, 1 / 18, 1 / 2]

dark, light = shades(col.draws, 2)
fig, ax = plt.subplots()
ax.plot(m, T1_bar, color=dark, label=r"$\bar T_1$")
ax.plot(m, T2_bar, color=light, label=r"$\bar T_2$")
ax.plot(m, S2_T1, color="tab:olive", label=r"$S^2_{T_1}$")
ax.plot(m, S2_T2, color="tab:orange", label=r"$S^2_{T_2}$")
ax.plot(m, r, color="tab:brown", label=r"$r(T_1,T_2)$")
ax.hlines(limits, m[0], m[-1], color=col.ref, ls="--")
ax.set(xscale="log", xlabel="$m$", ylabel="estimate")
ax.legend()

plt.show()
