# Negative log-likelihood of $(\mu,\sigma^2)$ and the path of the optimiser to its minimum
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

x = np.array([1.1, 0.9, 1.4, 1.0, 1.2])


def nll(mu, s2):
    """Negative log-likelihood; mu and s2 can be arrays."""
    sigma = np.sqrt(s2)[..., None]
    logpdf = norm.logpdf(x, mu[..., None], sigma)
    return -np.sum(logpdf, axis=-1)


mu_grid, s2_grid = np.meshgrid(np.linspace(0.8, 1.4, 101),
                               np.linspace(0.01, 0.3, 101))

path = []
result = minimize(lambda p: nll(p[0], p[1]), [1.0, 0.3],
                  bounds=[(None, None), (1e-9, None)],
                  callback=lambda p: path.append(p.copy()))
path = np.array(path)
mu_hat, s2_hat = result.x
print(f"minimum at mu = {mu_hat:.3f},"
      f" sigma^2 = {s2_hat:.4f}")

fig, ax = plt.subplots()
nll_grid = nll(mu_grid, s2_grid)
contour = ax.contourf(mu_grid, s2_grid, nll_grid, 100,
                      vmax=5, cmap="Purples_r")
bar = fig.colorbar(contour, ax=ax, location="top",
                   label="neg. log-likelihood")
bar.locator = plt.MaxNLocator(4)
bar.update_ticks()
ax.plot(path[:, 0], path[:, 1], "o-", color=col.path, ms=3)
ax.set_xlabel(r"$\mu$")
ax.set_ylabel(r"$\sigma^2$")

plt.show()
