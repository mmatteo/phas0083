# Running variance of $R=X/Y$ for $N$ up to $2\times10^6$ draws, and the delta-method value
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

mu_X, sd_X = 10.0, 1.0
mu_Y, sd_Y = 3.0, 1.0   # 3 standard deviations from 0

dR_dX = 1 / mu_Y
dR_dY = -mu_X / mu_Y**2
var_delta = dR_dX**2 * sd_X**2 + dR_dY**2 * sd_Y**2
print(f"delta method: Var(R) ~ {var_delta:.3f}")

rng = np.random.default_rng(7)
N = 2_000_000
X = rng.normal(mu_X, sd_X, N)
Y = rng.normal(mu_Y, sd_Y, N)
R = X / Y

steps = np.logspace(3, np.log10(N), 40).astype(int)
steps = np.unique(steps)
running_var = [np.var(R[:n], ddof=1) for n in steps]

fig, ax = plt.subplots()
ax.plot(steps, running_var, "o-", color=col.emp)
ax.axhline(var_delta, **ref, label="delta method")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("$N$")
ax.set_ylabel("running Var$(R)$")
ax.legend()

plt.show()
