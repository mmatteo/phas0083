# Sample of 60 values from the peak-over-background model, with $\hat\mu$ and its 90\% confidence interval
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

x = np.concatenate([rng.normal(0.5, 1, 40),
                    rng.uniform(-4, 4, 20)])
sigma = 1.0
alpha = 0.10


def chisq_lrt(mu_0, x, sigma):
    """Likelihood-ratio statistic for the mean."""
    return x.size * ((x.mean() - mu_0) / sigma)**2


mu_hat = x.mean()
mu_grid = np.linspace(mu_hat - 3, mu_hat + 3, 1000)
T = chisq_lrt(mu_grid, x, sigma)
inside = T <= chi2.ppf(1 - alpha, df=1)
low, high = mu_grid[inside].min(), mu_grid[inside].max()
print(f"mu_hat = {mu_hat:.2f}, I = [{low:.2f}, {high:.2f}]")

fig, ax = plt.subplots()
ax.hist(x, color=col.hist)
ax.axvline(mu_hat, color=col.data,
           label=r"$\hat\mu$")
ax.axvline(low, **thr, label="$I$")
ax.axvline(high, **thr)
ax.set_xlabel("$x$")
ax.set_ylabel("counts")
ax.legend()

plt.show()
