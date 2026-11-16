# Example 3.5.6 (Figure 3.15): Observed numbers of 10-s intervals with a given number of IMB events, and the Poisson expectation with $\nu=0.77$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

obs = np.array([1043, 860, 307, 78, 15, 3, 0, 0, 1, 0, 0])
n = obs.sum()
nu = 0.77
k = 8
x = np.arange(obs.size)
expected = n * poisson.pmf(x, nu)

p_eq = poisson.pmf(k, nu)
p_ge = 1 - poisson.cdf(k - 1, nu)
print(f"P(N={k} | nu={nu}) = {p_eq:.3e}")
print(f"P(N>={k} | nu={nu}) = {p_ge:.3e}")
print(f"P(at least one N={k}) = {1 - (1 - p_eq)**n:.3e}")
print(f"P(at least one N>={k}) = {1 - (1 - p_ge)**n:.3e}")

fig, ax = plt.subplots()
ax.plot(x, expected, "o", color=col.pmf,
        fillstyle="none", label="Poisson")
ax.vlines(x, 0, expected, colors=col.pmf)
ax.plot(x, obs, "x", color=col.data, ms=7, mew=1.5,
        label="observed")
ax.set(yscale="log", xticks=x, xlabel="events in 10 s")
ax.set_ylabel("number of intervals")
ax.legend()

plt.show()
