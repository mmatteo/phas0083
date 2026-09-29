# Four sequential updates of a normal prior (top to bottom), each posterior becoming the next prior
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

mu, tau = 0.0, 1.0   # initial prior
sigma = 1.0
observations = [2.0, 1.5, 3.0, 2.2]
theta = np.linspace(-2, 4, 400)

fig, axes = plt.subplots(len(observations), 1, sharex=True)
for i, (ax, y) in enumerate(zip(axes, observations), 1):
    precision = 1 / tau**2 + 1 / sigma**2
    mu_new = (mu / tau**2 + y / sigma**2) / precision
    tau_new = np.sqrt(1 / precision)
    ax.plot(theta, norm.pdf(theta, mu, tau), color=col.hist,
            label="prior")
    ax.plot(theta, norm.pdf(theta, y, sigma),
            color=col.like, label="likelihood")
    ax.plot(theta, norm.pdf(theta, mu_new, tau_new),
            color=col.pdf,
            label="posterior")
    ax.set_title(f"update {i}: $y={y}$")
    ax.set_ylabel("density")
    mu, tau = mu_new, tau_new
axes[-1].set_xlabel(r"$\theta$")
axes[0].legend()

plt.show()
