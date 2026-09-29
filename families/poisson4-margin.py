# Observed numbers of 10-s intervals with a given number of IMB events, and the Poisson expectation with $\nu=0.77$
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

obs = np.array([1043, 860, 307, 78, 15, 3, 0, 0, 1, 0, 0])
n = obs.sum()
nu = 0.77
x = np.arange(0, 11)
expected = n * poisson.pmf(x, nu)

fig, ax = plt.subplots()
ax.vlines(x, 0, expected, colors=col.pdf)
ax.plot(x, expected, "o", color=col.pdf, fillstyle="none",
        label="Poisson")
ax.plot(x, obs, "x", color=col.data, ms=7, mew=1.5,
        label="observed")
ax.set_yscale("log")
ax.set_xlabel("events in 10 s")
ax.set_ylabel("number of intervals")
ax.legend()

p_eq8 = poisson.pmf(8, nu)
p_ge8 = 1 - poisson.cdf(7, nu)
p_atleast1_eq8 = 1 - (1 - p_eq8)**n
p_atleast1_ge8 = 1 - (1 - p_ge8)**n
print(f"P(N=8 | nu=0.77) = {p_eq8:.6e}")
print(f"P(N>=8 | nu=0.77) = {p_ge8:.6e}")
print(f"P(at least one N=8) = {p_atleast1_eq8:.3e}")
print(f"P(at least one N>=8) = {p_atleast1_ge8:.3e}")

plt.show()
