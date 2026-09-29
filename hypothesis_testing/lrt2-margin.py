# Likelihood of $\mu$ with $\sigma^2$ at its restricted and unrestricted MLEs, and the resulting likelihood ratio
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

x = np.array([1.1, 0.9, 1.4, 1.0, 1.2])


def likelihood(mu, s2):
    """Product of the normal pdfs; mu can be an array."""
    mu = np.array(mu).reshape(-1, 1)
    return np.prod(norm.pdf(x, mu, np.sqrt(s2)), axis=1)


mu_0 = min(1.0, x.mean())        # MLE under H0: mu <= 1
s2_0 = np.mean((x - mu_0)**2)
mu_hat = x.mean()                # unrestricted MLE
s2_hat = np.mean((x - mu_hat)**2)
L_0 = likelihood(mu_0, s2_0)[0]
L_hat = likelihood(mu_hat, s2_hat)[0]
ratio = L_0 / L_hat

mu = np.linspace(0.8, 1.4, 200)
cases = [(mu_0, s2_0, ":", r"$\hat\sigma_0^2$"),
         (mu_hat, s2_hat, "-.", r"$\hat\sigma^2$")]
fig, ax = plt.subplots()
for color, (m, s2, dash, label) in zip(shades(col.like, 2),
                                       cases):
    ax.plot(mu, likelihood(mu, s2), color=color,
            label=label)
    L = likelihood(m, s2)
    ax.vlines(m, 0, L, color=col.thr, ls=dash)
    ax.hlines(L, 0.8, m, color=col.thr, ls=dash)
ax.set_title(rf"$\lambda(\mathbf{{x}})={ratio:.3f}$")
ax.set_xlabel(r"$\mu$")
ax.set_ylabel("likelihood")
ax.legend()

plt.show()
