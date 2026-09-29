# Pmf and cdf of the number of detected gamma-rays, binomial with $n=20$, $p=0.1$
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

n = 20
p = 0.1
x = np.arange(0, n + 1)
pmf = binom.pmf(x, n, p)
cdf = binom.cdf(x, n, p)

fig, ax = plt.subplots()
ax.plot(x, pmf, "o", color=col.pdf, label="pmf")
ax.vlines(x, 0, pmf, colors=col.pdf)
ax.plot(x, cdf, "o", color=col.cdf, label="cdf")
ax.hlines(cdf, x, x + 1, colors=col.cdf)
ax.set_xlabel("$y$")
ax.set_ylabel("probability")
ax.legend()

print(f"P(Y = 1) = {binom.pmf(1, n, p):.4f}")
print(f"P(Y >= 1) = {1 - binom.cdf(0, n, p):.4f}")
print(f"P(Y < 1) = {binom.cdf(0, n, p):.4f}")

plt.show()
