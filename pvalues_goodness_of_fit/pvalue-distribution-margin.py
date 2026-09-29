# Distribution of the p-value of a test of $\mu=0$ over 10000 samples: uniform under $H_0$ (top), piled up near zero under $H_1$ (bottom)
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

n, sigma = 10, 1
B = 10_000


def p_values(mu):
    """Two-sided p-values of the z test of mu = 0."""
    x = rng.normal(mu, sigma, (B, n))
    z = x.mean(axis=1) / (sigma / np.sqrt(n))
    return 2 * norm.sf(np.abs(z))


fig, axes = plt.subplots(2, 1, sharex=True)
labels = [r"$H_0$: $\mu=0$", r"$H_1$: $\mu=0.8$"]
for ax, mu, label in zip(axes, [0, 0.8], labels):
    p = p_values(mu)
    ax.hist(p, bins=20, range=(0, 1), density=True,
            color=col.hist)
    ax.axhline(1, **ref)
    ax.set_title(label)
    ax.set_ylabel("density")
    print(f"{label}: P(p < 0.05) = {np.mean(p < 0.05):.3f}")
axes[1].set_xlabel("p-value")

plt.show()
