# Prior $\mathcal{N}(0,1)$, likelihood of the observation $y=2$ with $\sigma=1$, and posterior of $\theta$
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

mu_0, tau_0 = 0.0, 1.0   # prior
sigma, y = 1.0, 2.0      # observation

precision = 1 / tau_0**2 + 1 / sigma**2
mu_1 = (mu_0 / tau_0**2 + y / sigma**2) / precision
tau_1 = np.sqrt(1 / precision)

theta = np.linspace(mu_0 - 4 * tau_0, y + 4 * sigma, 500)
fig, ax = plt.subplots()
ax.plot(theta, norm.pdf(theta, mu_0, tau_0), color=col.hist,
        label="prior")
ax.plot(theta, norm.pdf(theta, y, sigma), color=col.like,
        label="likelihood")
ax.plot(theta, norm.pdf(theta, mu_1, tau_1), color=col.pdf,
        label="posterior")
ax.set_xlabel(r"$\theta$")
ax.set_ylabel("density")
ax.legend()

plt.show()
