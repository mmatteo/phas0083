# Error of the estimated $P(-1<X<1)$ against $N$ in four runs, and the predicted binomial precision
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

p_true = norm.cdf(1) - norm.cdf(-1)   # P(-1 < X < 1)
N_values = np.array([10, 30, 100, 300, 1000, 3000,
                     1e4, 3e4, 1e5, 3e5, 1e6], dtype=int)

fig, ax = plt.subplots()
for color in shades(col.emp, 4):  # four independent runs
    x = rng.normal(0, 1, N_values[-1])
    inside = np.abs(x) < 1
    p_hat = np.cumsum(inside)[N_values - 1] / N_values
    ax.plot(N_values, np.abs(p_hat - p_true), "o-",
            color=color)

# binomial precision: std of the estimate, sqrt(p(1-p)/N)
sd = np.sqrt(p_true * (1 - p_true) / N_values)
ax.plot(N_values, sd, **ref, label=r"$\sqrt{p(1-p)/N}$")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("$N$")
ax.set_ylabel(r"$|\hat{F}_N - p|$")
ax.legend()

plt.show()
