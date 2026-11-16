# Example 5.6.2 (Figure 5.18): ecdf of $N=10^6$ draws of $Y=X^2$, $X\sim\mathcal{N}(10,2^2)$, with the exact cdf and the normal cdf of the delta method (top), and its lower tail (bottom)
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

mu = 10.0
sigma = 2.0
var_exact = 4 * mu**2 * sigma**2 + 2 * sigma**4
var_delta = 4 * mu**2 * sigma**2

N = 1_000_000
y = rng.normal(mu, sigma, size=N)**2

print(f"exact: {var_exact:.0f}  delta: {var_delta:.0f}")
print(f"draws: var {y.var():.0f}, mean {y.mean():.0f}")

u = np.linspace(20, 260, 400)
F_exact = norm.cdf(np.sqrt(u), mu, sigma)
F_delta = norm.cdf(u, mu**2, np.sqrt(var_delta))
fig, axes = plt.subplots(2, 1)
for ax, lim in zip(axes, [(20, 260), (30, 90)]):
    ax.plot(u, F_exact, color=col.cdf, label="exact $F_Y$")
    ax.plot(u, F_delta, color=col.ref, ls="--",
            label="delta method")
    ax.ecdf(y, color=col.draws, ls=":",
            label=r"$\hat{F}_N$")
    ax.set(xlim=lim, ylabel="cdf")
axes[1].set(ylim=(0, 0.35), xlabel="$y$")
axes[0].legend()

plt.show()
