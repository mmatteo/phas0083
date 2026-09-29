# Survival function of the test statistic under $H_0$, with the threshold for $\alpha=5\%$ and the observed value
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

def nlrt(x, lambda_0, nu):
    """-2 log likelihood ratio of the on/off model."""
    lambda_hat = np.maximum(0, x - nu)
    return (-2 * poisson.logpmf(x, lambda_0 + nu)
            + 2 * poisson.logpmf(x, lambda_hat + nu))


lambda_0, nu, alpha = 1000, 1000, 0.05
x_star = rng.poisson(lambda_0 + nu, size=1_000_000)
T = nlrt(x_star, lambda_0, nu)
c = np.quantile(T, 1 - alpha)
t_obs = nlrt(2100, lambda_0, nu)

t = np.linspace(0, T.max(), 2000)
fig, ax = plt.subplots()
ax.plot(t, chi2.sf(t, df=1), color=col.cdf)
for value, style, label in [
        (c, thr, "$c$"),
        (t_obs, dict(color=col.data),
         r"$\tilde\lambda(x_\mathrm{obs})$")]:
    ax.axvline(value, label=label, **style)
    ax.hlines(chi2.sf(value, df=1), 0, value, **style)
ax.set_xlim(0, 6)
ax.set_ylim(0, 0.1)
ax.set_xlabel(r"$\tilde\lambda(x)$")
ax.set_ylabel(r"$1-F$ = p-value")
ax.legend()

plt.show()
