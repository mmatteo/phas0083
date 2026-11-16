# Example 10.1.11 (Figure 10.4): Test statistic of the sample $\mathbf{x}$ over $(\mu,\sigma^2)$, with the 68\%, 95\% and 99\% confidence regions from Wilks' theorem
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([1.1, 0.9, 1.4, 1.0, 1.2])


def log_l(mu, s2):
    total = 0
    for xi in x:
        total = total + norm.logpdf(xi, mu, np.sqrt(s2))
    return total


def nlrt(mu_0, s2_0):
    mu_hat = x.mean()
    s2_hat = x.var(ddof=0)
    return -2 * (log_l(mu_0, s2_0) - log_l(mu_hat, s2_hat))


# compute the statistic on a grid and the thresholds
mu_grid, s2_grid = np.meshgrid(np.linspace(0.8, 1.4, 101),
                               np.linspace(0.01, 0.3, 101))
T = nlrt(mu_grid, s2_grid)
levels = [0.68, 0.95, 0.99]
c_values = chi2.ppf(levels, df=2)

fig, ax = plt.subplots()
filled = ax.contourf(mu_grid, s2_grid, T, levels=300,
                     vmax=10, cmap="Purples_r")
fig.colorbar(filled, label=r"$-2\log\lambda(\mathbf{x})$",
             location="top", ticks=MaxNLocator(4))
lines = ax.contour(mu_grid, s2_grid, T, levels=c_values,
                   colors="tab:orange")
ax.clabel(lines, fmt={c: f"{p:.0%}"
                      for c, p in zip(c_values, levels)})
ax.set(xlabel=r"$\mu$", ylabel=r"$\sigma^2$")

plt.show()
