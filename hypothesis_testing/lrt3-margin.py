# Negative log-likelihood of $(\mu,\sigma^2)$ with the optimiser paths to the unrestricted and restricted ($\mu\leq1$) minima
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
    mu = np.atleast_1d(mu)[..., None]
    sigma = np.atleast_1d(np.sqrt(s2))[..., None]
    return -np.sum(norm.logpdf(x, mu, sigma), axis=-1)


def minimise(mu_max):
    """Minimise the NLL for mu <= mu_max."""
    path = [np.array([0.9, 0.25])]
    result = minimize(
        lambda p: nll(p[0], p[1]), x0=path[0],
        bounds=[(None, mu_max), (1e-9, None)],
        callback=lambda p: path.append(p.copy()))
    return result, np.array(path)


free, path_free = minimise(None)
restricted, path_restricted = minimise(1)
test = float(2 * (restricted.fun - free.fun))
print(f"-2 log lambda(x) = {test:.3f}")

mu_grid, s2_grid = np.meshgrid(np.linspace(0.8, 1.4, 101),
                               np.linspace(0.01, 0.3, 101))
fig, ax = plt.subplots()
ax.contourf(mu_grid, s2_grid, nll(mu_grid, s2_grid), 100,
            vmax=5, cmap="Purples_r")
ax.axvline(1, **ref)
ax.plot(*path_free.T, "o-", color=col.path, ms=3,
        label="unrestricted")
ax.plot(*path_restricted.T, "s--", color=col.path, ms=3,
        label=r"$\mu\leq1$")
ax.set_title(rf"$-2\log\lambda(\mathbf{{x}})={test:.3f}$")
ax.set_xlabel(r"$\mu$")
ax.set_ylabel(r"$\sigma^2$")
ax.legend()

plt.show()
