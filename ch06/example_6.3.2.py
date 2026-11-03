# Example 6.3.2 (Figure 6.8): Sample mean, variance and correlation of the arrival times on the first $m$ observations, with the population values
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

N = 10_000
U1 = rng.uniform(0, 1, size=N)
U2 = rng.uniform(0, 1, size=N)
T1 = np.minimum(U1, U2)
T2 = np.maximum(U1, U2)

# the statistics on the first m observations, m = 10, ..., N
m = np.arange(10, N + 1)
T1_bar = [T1[:i].mean() for i in m]
T2_bar = [T2[:i].mean() for i in m]
S2_T1 = [T1[:i].var(ddof=1) for i in m]
S2_T2 = [T2[:i].var(ddof=1) for i in m]
r = [np.corrcoef(T1[:i], T2[:i])[0, 1] for i in m]

# population values, E T1, E T2, Var T1 = Var T2 and rho
E_T1, E_T2, var, rho = 1 / 3, 2 / 3, 1 / 18, 0.5

# an exception to the palette: five curves on one panel need
# more contrast than shades of green give
colors = ["#1b5e20", "#43a047", "#9ccc65",
          "#fbc02d", "#e65100"]
fig, ax = plt.subplots()
ax.plot(m, T1_bar, color=colors[0], label=r"$\bar T_1$")
ax.plot(m, T2_bar, color=colors[1], label=r"$\bar T_2$")
ax.plot(m, S2_T1, color=colors[2], label=r"$S^2_{T_1}$")
ax.plot(m, S2_T2, color=colors[3], label=r"$S^2_{T_2}$")
ax.plot(m, r, color=colors[4], label=r"$r(T_1,T_2)$")
for value in [E_T1, E_T2, var, rho]:
    ax.axhline(value, **ref)
ax.set_xscale("log")
ax.set_xlabel("$m$")
ax.set_ylabel("estimate")
ax.legend()

plt.show()
