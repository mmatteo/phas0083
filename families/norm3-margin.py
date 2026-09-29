# Binomial pmf with $p=0.3$ for increasing $n$, and the normal approximation for $n=100$
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

p = 0.3
x = np.arange(0, 45)

fig, ax = plt.subplots()
for color, n in zip(shades(col.pdf, 3), [10, 30, 100]):
    pmf = binom.pmf(x, n, p)
    ax.plot(x, pmf, "o", color=color, label=f"$n={n}$")
    ax.vlines(x, 0, pmf, colors=[color])

mu = 100 * p
sigma = np.sqrt(100 * p * (1 - p))
u = np.linspace(0, 45, 400)
ax.plot(u, norm.pdf(u, mu, sigma), **ref, label="normal")
ax.set_xlabel("$x$")
ax.set_ylabel("probability")
ax.legend()

plt.show()
