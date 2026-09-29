# Thirty 90\% confidence intervals for $\mu$ from repeated samples of size 10: those that miss $\mu$ (dashed line) are in red
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

mu, sigma, n = 0, 1, 10
z = norm.ppf(0.95)
B = 30

fig, ax = plt.subplots()
missed = 0
for b in range(B):
    x = rng.normal(mu, sigma, n)
    half = z * sigma / np.sqrt(n)
    lo, hi = x.mean() - half, x.mean() + half
    covers = lo <= mu <= hi
    missed += not covers
    color = col.emp if covers else "#d62728"
    ax.plot([lo, hi], [b, b], color=color)
    ax.plot(x.mean(), b, "o", ms=2, color=col.data)
ax.axvline(mu, **ref)
ax.set_xlabel(r"$\bar{x} \pm 1.64\,\sigma/\sqrt{n}$")
ax.set_ylabel("sample")
ax.set_yticks([0, 10, 20, 29])
print(f"intervals missing mu: {missed} of {B}")

plt.show()
