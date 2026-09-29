# Power functions of the two tests of $H_0:\theta\le1/2$ based on five Bernoulli trials
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

def beta_1(theta):
    """Reject if all five trials succeed."""
    return theta**5


def beta_2(theta):
    """Reject if at least three trials succeed."""
    return (comb(5, 3) * theta**3 * (1 - theta)**2
            + comb(5, 4) * theta**4 * (1 - theta)
            + comb(5, 5) * theta**5)


theta = np.linspace(0, 1, 400)
fig, ax = plt.subplots()
color_1, color_2 = shades(col.cdf, 2)
ax.plot(theta, beta_1(theta), color=color_1,
        label=r"$\beta_1$")
ax.plot(theta, beta_2(theta), color=color_2,
        label=r"$\beta_2$")
ax.axvline(1 / 2, **ref)
ax.set_xlabel(r"$\theta$")
ax.set_ylabel("power")
ax.legend()

plt.show()
