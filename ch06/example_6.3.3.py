# Example 6.3.3 (Figure 6.9): Sample mean, variance and correlation of the arrival times on the first $m$ observations, with the population values
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

E_T1, E_T2, var, rho = 1 / 3, 2 / 3, 1 / 18, 0.5

rng = np.random.default_rng(40)
N = 10_000
U1, U2 = rng.uniform(0, 1, size=(2, N))
T1, T2 = np.minimum(U1, U2), np.maximum(U1, U2)

# from m = 2: variance and correlation need two values
m = np.arange(2, N + 1)
stats_m = {
    r"$\bar T_1$": [T1[:i].mean() for i in m],
    r"$\bar T_2$": [T2[:i].mean() for i in m],
    r"$S^2_{T_1}$": [T1[:i].var(ddof=1) for i in m],
    r"$S^2_{T_2}$": [T2[:i].var(ddof=1) for i in m],
    r"$r(T_1,T_2)$": [np.corrcoef(T1[:i], T2[:i])[0, 1]
                      for i in m],
}

# an exception to the palette: five curves on one panel need
# more contrast than shades of green give
colors = ["#1b5e20", "#43a047", "#9ccc65",
          "#fbc02d", "#e65100"]
fig, ax = plt.subplots()
for color, (label, values) in zip(colors, stats_m.items()):
    ax.plot(m, values, color=color, label=label)
for value in [E_T1, E_T2, var, rho]:
    ax.axhline(value, **ref)
ax.set_xscale("log")
ax.set_xlabel("$m$")
ax.set_ylabel("estimate")
ax.legend()

plt.show()
