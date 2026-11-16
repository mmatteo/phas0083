# Example 8.5.4 (Figure 8.12): Power of the level-0.05 test as a function of the signal $\lambda$, with the background known
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

nu = 50
m = 10_000
lam_values = np.linspace(0, 30, 20)
c = 2.674  # the threshold of the previous example


def nlrt(x, nu):
    lam_hat = np.maximum(0, x - nu)
    return (-2 * poisson.logpmf(x, nu)
            + 2 * poisson.logpmf(x, lam_hat + nu))


# power at each lambda: the fraction of counts rejected
power = []
for lam in lam_values:
    x = rng.poisson(lam + nu, size=m)
    power.append(np.mean(nlrt(x, nu) > c))

fig, ax = plt.subplots()
ax.plot(lam_values, power, "o-", color=col.draws)
ax.set(xlabel=r"$\lambda$", ylabel="power")

plt.show()
