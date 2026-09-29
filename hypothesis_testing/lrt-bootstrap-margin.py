# Bootstrap distribution of the likelihood-ratio statistic under $H_0$ (top) and its survival function (bottom), with the level-0.05 threshold
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

def log_l(x, y, lam, nu, tau):
    """On/off log-likelihood, up to constant terms."""
    nu = nu if nu > 0 else 1e-12
    lam = lam if lam > 0 else 1e-12
    return (x * np.log(lam + nu) - (lam + nu)
            + y * np.log(tau * nu) - tau * nu)


def lrt(x, y, tau):
    """-2 log of the likelihood ratio for H0: lambda = 0."""
    if x <= y / tau:
        return 0.0
    nu_0 = (x + y) / (1 + tau)           # MLE under H0
    # unrestricted MLE
    nu_hat, lam_hat = y / tau, x - y / tau
    return -2 * (log_l(x, y, 0.0, nu_0, tau)
                 - log_l(x, y, lam_hat, nu_hat, tau))


tau, nu, B = 2.0, 50, 100_000
x = rng.poisson(nu, size=B)
y = rng.poisson(tau * nu, size=B)
T = np.array([lrt(xi, yi, tau) for xi, yi in zip(x, y)])
c = np.quantile(T, 1 - 0.05)
print(f"threshold for level 0.05: T > {c:.3f}")

fig, axes = plt.subplots(2, 1, sharex=True)
axes[0].hist(T, density=True, bins=40, color=col.hist)
axes[0].set_yscale("log")
axes[0].set_ylabel("density")
survival = np.linspace(1, 0, B, endpoint=False)
axes[1].plot(np.sort(T), survival, color=col.cdf)
axes[1].set_ylabel("survival")
axes[1].set_xlabel("$T$")
for ax in axes:
    ax.axvline(c, **thr)

plt.show()
