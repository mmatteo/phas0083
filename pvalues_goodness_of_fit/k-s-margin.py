# Empirical cdf of a uniform sample of 20 and the cdf of the normal model tested by Kolmogorov--Smirnov
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

x = rng.uniform(-3, 3, size=20)
ks = stats.kstest(x, norm.cdf)
print(f"D = {ks.statistic:.3f}, p-value = {ks.pvalue:.1g}")

u = np.linspace(-3, 3, 100)
fig, ax = plt.subplots()
F_hat = np.linspace(0, 1, x.size, endpoint=False)
ax.step(np.sort(x), F_hat, color=col.emp, label="data")
ax.plot(u, norm.cdf(u), color=col.cdf, label="model")
ax.plot(x, np.zeros_like(x), "|", color=col.data, ms=8)
ax.set_xlabel("$x$")
ax.set_ylabel("cdf")
ax.legend()

plt.show()
