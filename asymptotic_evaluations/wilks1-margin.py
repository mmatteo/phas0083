# Bootstrap distribution of the test statistic under $H_0$, the chi-squared prediction and the level-0.05 threshold
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
threshold = np.quantile(T, 1 - alpha)
print(f"level {alpha}: reject if T > {threshold:.3f}")

fig, ax = plt.subplots()
_, bins, _ = ax.hist(T, bins=50, density=True,
                     color=col.hist)
# chi-squared probability of each bin, per unit width
chi2_density = np.diff(chi2.cdf(bins, df=1)) / np.diff(bins)
centres = (bins[:-1] + bins[1:]) / 2
ax.plot(centres, chi2_density, **ref,
        label=r"$\chi^2_1$")
ax.axvline(threshold, **thr)
ax.set_xlim(0, 15)
ax.set_yscale("log")
ax.set_xlabel(r"$\tilde\lambda$")
ax.set_ylabel("density")
ax.legend()

plt.show()
