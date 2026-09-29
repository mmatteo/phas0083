# Estimated 0.05 and 0.95 quantiles of $t^*-t$ against $B$
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

x = np.array([3.54, 5.13, 2.84, 4.48, 1.03, 16.92,
              0.05, 14.05, 2.88, 1.50, 2.71, 1.56])
n = x.size
x_bar = x.mean()
B_values = [19, 39, 99, 199, 399, 599, 799, 999]

fig, ax = plt.subplots()
for color in shades(col.emp, 4):  # four independent runs
    q05, q95 = [], []
    for B in B_values:
        x_star = rng.exponential(scale=x_bar, size=(B, n))
        d = np.sort(x_star.mean(axis=1)) - x_bar
        q05.append(d[int((B + 1) * 0.05) - 1])
        q95.append(d[int((B + 1) * 0.95) - 1])
    ax.plot(B_values, q05, "o-", color=color)
    ax.plot(B_values, q95, "o-", color=color)

# exact: the mean of n exponentials is Gamma(n, x_bar/n)
for p in [0.05, 0.95]:
    q = stats.gamma.ppf(p, n, scale=x_bar / n) - x_bar
    ax.axhline(q, **ref)
ax.set_xscale("log")
ax.set_xlabel("$B$")
ax.set_ylabel("quantiles of $t^* - t$")

plt.show()
