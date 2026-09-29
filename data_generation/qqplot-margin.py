# Q-Q plots of $N=10$ (top) and $N=100$ (bottom) draws from $\mathcal{N}(0,1)$ against the normal quantiles
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

lims = [-4, 4]

fig, axes = plt.subplots(2, 1, sharex=True)
for ax, N in zip(axes, [10, 100]):
    x = np.sort(rng.normal(0, 1, N))
    # plotting positions
    p = (np.arange(1, N + 1) - 0.5) / N
    ax.plot(lims, lims, **ref)
    ax.plot(norm.ppf(p), x, "o", color=col.emp, ms=2)
    ax.set_xlim(lims)
    ax.set_ylim(lims)
    ax.set_title(f"$N={N}$")
    ax.set_ylabel("sample quantile")
axes[-1].set_xlabel("theoretical quantile")

plt.show()
