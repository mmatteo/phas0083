# Draws from $f(x)=2x$ by inverse-transform (top) and rejection (bottom) sampling, with the pdf
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

N = 20000

# inverse transform: F(x) = x^2, so x = sqrt(u)
u = rng.uniform(0, 1, N)
x_inv = np.sqrt(u)

# rejection: envelope uniform on [0, 1] x [0, 2]
x_env = rng.uniform(0, 1, 3 * N)
v_env = rng.uniform(0, 2, 3 * N)
accepted = x_env[v_env <= 2 * x_env]
efficiency = accepted.size / (3 * N)
x_rej = accepted[:N]
print(f"rejection efficiency: {efficiency:.2f}"
      " (expected 0.50)")

t = np.linspace(0, 1, 200)
fig, axes = plt.subplots(2, 1, sharex=True)
for ax, x, title in zip(axes, [x_inv, x_rej],
                        ["inverse transform", "rejection"]):
    ax.hist(x, bins=20, density=True, color=col.hist)
    ax.plot(t, 2 * t, **ref)
    ax.set_title(title)
    ax.set_ylabel("density")
axes[-1].set_xlabel("$x$")

plt.show()
