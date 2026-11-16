# Example 9.1.8 (Figure 9.4): Coverage probability of the interval $[I_\mathrm{low}(X),1]$ for $X\sim\mathrm{Binomial}(5,\theta)$, as a function of $\theta$; the vertical lines are the six values of $I_\mathrm{low}$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

N = 5
I_low = [0, 0.01, 0.07, 0.18, 0.34, 0.54]
theta = np.linspace(0, 1, 1001)

# coverage: add the pmf of the x with I_low below theta
coverage = np.zeros_like(theta)
for x, low in enumerate(I_low):
    coverage += binom.pmf(x, N, theta) * (low <= theta)
print(f"smallest coverage: {coverage.min():.2f}")

fig, ax = plt.subplots()
ax.plot(theta, coverage, color=col.cdf)
ax.vlines(I_low, 0.94, 1, color=col.ref, ls=":", lw=0.8)
ax.axhline(0.95, color=col.ref, ls=":")
ax.set(ylim=(0.94, 1.002), xlabel=r"$\theta$",
       ylabel="coverage probability")

plt.show()
