# Bootstrap estimates of the bias (top) and variance (bottom) of the mean against $B$, in four runs
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
B_values = [10, 20, 50, 100, 200, 500, 1000, 2000]

fig, axes = plt.subplots(2, 1, sharex=True)
for color in shades(col.emp, 4):  # four independent runs
    bias_B, var_B = [], []
    for B in B_values:
        x_star = rng.exponential(scale=x_bar, size=(B, n))
        t_star = x_star.mean(axis=1)
        bias_B.append(t_star.mean() - x_bar)
        var_B.append(t_star.var(ddof=1))
    axes[0].plot(B_values, bias_B, "o-", color=color)
    axes[1].plot(B_values, var_B, "o-", color=color)

# exact values under the fitted model
axes[0].axhline(0, **ref)
axes[1].axhline(x_bar**2 / n, **ref)
axes[0].set_ylabel("bias")
axes[1].set_ylabel("variance")
axes[1].set_xscale("log")
axes[1].set_xlabel("$B$")

plt.show()
