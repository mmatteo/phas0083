# Simulated $P=VI$ with small (top) and large (bottom) relative uncertainties, and normal pdfs with the exact and delta-method variances
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

rng = np.random.default_rng(1)
N = 2_000_000
cases = [(12, 0.5, 2, 0.1, "small uncertainties"),
         (12, 3, 2, 0.5, "large uncertainties")]

fig, axes = plt.subplots(2, 1)
for ax, (mu_V, sd_V, mu_I, sd_I, title) in zip(axes, cases):
    var_delta = mu_V**2 * sd_I**2 + mu_I**2 * sd_V**2
    missing = sd_V**2 * sd_I**2
    var_exact = var_delta + missing

    V = rng.normal(mu_V, sd_V, N)
    I = rng.normal(mu_I, sd_I, N)  # noqa: E741
    P = V * I
    bias = 100 * missing / var_exact
    print(f"{title}:")
    print(f"  exact {var_exact:.4f}, delta {var_delta:.4f}")
    var_sim = P.var(ddof=1)
    print(f"  missing {missing:.4f}, sim {var_sim:.4f}")
    print(f"  bias {bias:.2f}%")

    u = np.linspace(P.min(), P.max(), 200)
    ax.hist(P, bins=30, density=True, color=col.hist,
            label="simulation")
    ax.plot(u, norm.pdf(u, mu_V * mu_I, var_exact**0.5),
            **ref, label="exact")
    ax.plot(u, norm.pdf(u, mu_V * mu_I, var_delta**0.5),
            color=col.ref, ls="-.", label="delta")
    ax.set_title(title)
    ax.set_xlabel("$P$")
    ax.set_ylabel("density")
axes[0].legend()

plt.show()
