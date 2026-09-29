# Test statistic of the sample $\mathbf{x}$ over $(\mu,\sigma^2)$, with the 68\%, 95\% and 99\% confidence regions from Wilks' theorem
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x_obs = np.array([1.1, 0.9, 1.4, 1.0, 1.2])


def log_l(x, mu, s2):
    """Normal log-likelihood; sample along axis 0."""
    return np.sum(norm.logpdf(x, mu, np.sqrt(s2)), axis=0)


def nlrt(x, mu_0, s2_0):
    """-2 log likelihood ratio against the MLEs."""
    mu_hat, s2_hat = x.mean(), x.var(ddof=0)
    return -2 * (log_l(x, mu_0, s2_0)
                 - log_l(x, mu_hat, s2_hat))


mu_grid, s2_grid = np.meshgrid(np.linspace(0.8, 1.4, 101),
                               np.linspace(0.01, 0.3, 101))
T = nlrt(x_obs[:, None, None], mu_grid, s2_grid)
levels = [0.68, 0.95, 0.99]
thresholds = [chi2.ppf(p, df=2) for p in levels]

fig, ax = plt.subplots()
filled = ax.contourf(mu_grid, s2_grid, T, 300, vmax=10,
                     cmap="Purples_r")
bar = fig.colorbar(filled, ax=ax, location="top",
             label=r"$\tilde\lambda(\mathbf{x})$")
lines = ax.contour(mu_grid, s2_grid, T, levels=thresholds,
                   colors=col.path)
bar.locator = plt.MaxNLocator(4)
bar.update_ticks()
ax.clabel(lines, fmt={t: f"{100 * p:.0f}%"
                      for t, p in zip(thresholds, levels)})
ax.set_xlabel(r"$\mu$")
ax.set_ylabel(r"$\sigma^2$")

plt.show()
