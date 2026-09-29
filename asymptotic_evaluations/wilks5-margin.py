# Test statistic of the sample $\mathbf{x}$ over $(\mu,\sigma^2)$, with the 68\%, 95\% and 99\% confidence regions from Wilks' theorem
# Script of the lecture notes of PHAS0083 (UCL); the preamble below is shared by all scripts.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
from types import SimpleNamespace
from scipy import stats, optimize, integrate, special
from scipy.stats import (norm, poisson, binom, chi2,
                         expon, gamma, gaussian_kde)
from scipy.optimize import minimize, minimize_scalar
from math import comb

rng = np.random.default_rng(42)

# colours by kind of object (see the Coding Conventions)
col = SimpleNamespace(
    hist="#9ecae1",  # histogram of a sample; prior
    pdf="#1f77b4",   # pdf or pmf of a model; posterior
    cdf="#ff7f0e",   # cdf, survival function, power
    emp="#2ca02c",   # sampled points, EDF, KDE, runs
    like="#6a51a3",  # likelihood, likelihood ratio
    data="black",    # observed data and statistics
    ref="#525252",   # exact or approximate curve
    thr="#525252",   # threshold, critical value, reading
    path="#ff7f0e",  # line over a heat map: path, contour
)
ref = dict(color=col.ref, ls="--")  # style of exact curves
thr = dict(color=col.thr, ls=":")   # style of thresholds


def shades(color, n):
    """n shades of a colour: dark, itself, light."""
    rgb = np.array(to_rgb(color))
    dark, light = 0.35 * rgb, rgb + (1 - rgb) * 0.55
    result = []
    for t in np.linspace(0, 1, n):
        a, b, u = (dark, rgb, 2 * t) if t < 0.5 else \
            (rgb, light, 2 * t - 1)
        result.append(a + (b - a) * u)
    return result


# ------------------------------------------------------------

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
