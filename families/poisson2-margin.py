# Poisson pmf for $\nu=0.7,3,10$ (top); binomial pmf with $p=3/N$ approaching the Poisson with $\nu=3$ (bottom)
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

def poisson_modes(nu):
    """Modes of a Poisson: two if nu is an integer."""
    if abs(nu - round(nu)) < 1e-12:
        return int(nu - 1), int(nu)
    return (int(np.floor(nu)),)


x = np.arange(0, 21)
nu_values = [0.7, 3, 10]
nu_ref = 3                # mean of the binomial comparison
N_values = [5, 10, 100]   # p = nu_ref / N

fig, axes = plt.subplots(2, 1)
for color, nu in zip(shades(col.pdf, 3), nu_values):
    pmf = poisson.pmf(x, nu)
    axes[0].vlines(x, 0, pmf, colors=[color])
    axes[0].plot(x, pmf, "o", color=color,
                 label=rf"$\nu={nu}$")

# the Poisson is the limit the binomials approach
pmf_ref = poisson.pmf(x, nu_ref)
axes[1].vlines(x, 0, pmf_ref, colors=col.ref, alpha=0.4)
axes[1].plot(x, pmf_ref, "o", color=col.ref,
             fillstyle="none",
             label=rf"Poisson, $\nu={nu_ref}$")
for color, N in zip(shades(col.pdf, 3), N_values):
    pmf = binom.pmf(x, N, nu_ref / N)
    axes[1].plot(x, pmf, "x", color=color, mew=1.5,
                 label=f"binomial, $N={N}$")
axes[1].set_xlim(-0.5, 10.5)
for ax in axes:
    ax.set_ylabel("probability")
    ax.set_xlabel("number of occurrences")
    ax.legend()

print("Poisson modes:")
for nu in nu_values:
    print(f"  nu={nu}: {poisson_modes(nu)}")
print(f"Binomial modes, mean {nu_ref}:")
for N in N_values:
    mode = x[np.argmax(binom.pmf(x, N, nu_ref / N))]
    print(f"  N={N}: {mode}")

plt.show()
