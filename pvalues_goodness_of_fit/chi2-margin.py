# Observed counts of a uniform sample of 40 in seven bins, and the counts expected under $\mathcal{N}(0,1)$
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

n_bins = 7
x = rng.uniform(-3, 3, size=40)

edges = np.linspace(-3, 3, n_bins)
O, _ = np.histogram(x, bins=edges)  # noqa: E741
E = x.size * np.diff(norm.cdf(edges))
T = np.sum((O - E)**2 / E)
p_value = 1 - chi2.cdf(T, n_bins - 1)
print(f"T = {T:.1f}, p-value = {p_value:.2g}")

centres = (edges[1:] + edges[:-1]) / 2
fig, ax = plt.subplots()
ax.bar(centres, O, width=0.9, color=col.hist,
       label="observed")
ax.plot(centres, E, "o", color=col.ref, label="expected")
ax.set_xlabel("$x$")
ax.set_ylabel("counts")
ax.legend()

plt.show()
