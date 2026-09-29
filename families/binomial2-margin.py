# Binomial pmf for $n=5,10,20$ at $p=0.5$ (top) and for $p=0.1,0.2,0.6$ at $n=20$ (bottom)
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

def binom_mode(n, p):
    """Mode from the pmf, and the closed-form candidates."""
    x = np.arange(n + 1)
    pmf = binom.pmf(x, n, p)
    mode = x[np.argmax(pmf)]
    candidates = (int(np.floor((n + 1) * p)),
                  int(np.ceil((n + 1) * p) - 1))
    return mode, candidates, x, pmf


cases = [[(5, 0.5), (10, 0.5), (20, 0.5)],   # fixed p
         [(20, 0.1), (20, 0.2), (20, 0.6)]]  # fixed n

fig, axes = plt.subplots(2, 1, sharex=True)
for ax, row in zip(axes, cases):
    for color, (n, p) in zip(shades(col.pdf, 3), row):
        mode, _, x, pmf = binom_mode(n, p)
        label = f"$n={n}$, $p={p}$: mode {mode}"
        ax.vlines(x, 0, pmf, colors=[color])
        ax.plot(x, pmf, "o", color=color, label=label)
    ax.set_ylabel("probability")
    ax.legend()
axes[1].set_xlabel("number of successes")

print("mode from the pmf; floor((n+1)p), ceil((n+1)p)-1")
for n, p in cases[0] + cases[1]:
    mode, (c1, c2), _, _ = binom_mode(n, p)
    print(f"n={n:2d}, p={p}: {mode:2d}; {c1:2d}, {c2:2d}")

plt.show()
