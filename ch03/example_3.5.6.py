# Example 3.5.6 (Figure 3.12): Observed numbers of 10-s intervals with a given number of IMB events, and the Poisson expectation with $\nu=0.77$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

obs = np.array([1043, 860, 307, 78, 15, 3, 0, 0, 1, 0, 0])
n = obs.sum()
nu = 0.77
x = np.arange(0, 11)
expected = n * poisson.pmf(x, nu)

fig, ax = plt.subplots()
ax.vlines(x, 0, expected, colors=col.pdf)
ax.plot(x, expected, "o", color=col.pdf, fillstyle="none",
        label="Poisson")
ax.plot(x, obs, "x", color=col.data, ms=7, mew=1.5,
        label="observed")
ax.set_yscale("log")
ax.set_xlabel("events in 10 s")
ax.set_ylabel("number of intervals")
ax.legend()

p_eq8 = poisson.pmf(8, nu)
p_ge8 = 1 - poisson.cdf(7, nu)
p_atleast1_eq8 = 1 - (1 - p_eq8)**n
p_atleast1_ge8 = 1 - (1 - p_ge8)**n
print(f"P(N=8 | nu=0.77) = {p_eq8:.6e}")
print(f"P(N>=8 | nu=0.77) = {p_ge8:.6e}")
print(f"P(at least one N=8) = {p_atleast1_eq8:.3e}")
print(f"P(at least one N>=8) = {p_atleast1_ge8:.3e}")

plt.show()
