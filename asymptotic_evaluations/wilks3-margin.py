# Test statistic of $x_\mathrm{obs}=2050$ against $\lambda_0$, with the bootstrap and chi-squared level-0.05 thresholds
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


x_obs, nu, alpha = 2050, 1000, 0.05
lambda_values = np.linspace(900, 1200, 25)
obs = np.zeros_like(lambda_values)
threshold = np.zeros_like(lambda_values)
for i, lambda_0 in enumerate(lambda_values):
    obs[i] = nlrt(x_obs, lambda_0, nu)
    x_star = rng.poisson(lambda_0 + nu, size=100_000)
    T = nlrt(x_star, lambda_0, nu)
    threshold[i] = np.quantile(T, 1 - alpha)

fig, ax = plt.subplots()
ax.plot(lambda_values, obs, color=col.like,
        label="test value")
ax.plot(lambda_values, threshold, "x", color=col.thr,
        label="bootstrap")
ax.axhline(chi2.ppf(1 - alpha, df=1), **ref,
           label=r"$\chi^2_1$")
ax.set_xlabel(r"$\lambda_0$")
ax.set_ylabel("test statistic")
ax.legend()

plt.show()
