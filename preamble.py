import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex, to_rgb
from matplotlib.ticker import MaxNLocator
from types import SimpleNamespace
from scipy import stats
from scipy.stats import (norm, poisson, binom, chi2,
                         expon, gamma, gaussian_kde)
from scipy.optimize import minimize, minimize_scalar
from math import comb

rng = np.random.default_rng(42)

# colours by kind of object (see the Coding Conventions)
col = SimpleNamespace(
    pmf="#1f77b4",    # pmf of a model
    pdf="#1f77b4",    # pdf of a model
    cdf="#ff7f0e",    # cdf, survival function, power of a model
    data="black",     # observed data, statistics and estimates
    draws="#2ca02c",  # simulated draws, their ecdf and KDE
    hist="#9ecae1",   # fill of a histogram
    like="#6a51a3",   # likelihood, likelihood ratio
    ref="#525252",    # exact curve or true value (dashed);
)                     # threshold or reading (dotted)


def shades(color, n):
    """n shades of a colour: dark, itself, light."""
    rgb = np.array(to_rgb(color))
    dark, light = 0.35 * rgb, rgb + (1 - rgb) * 0.55
    result = []
    for t in np.linspace(0, 1, n):
        a, b, u = (dark, rgb, 2 * t) if t < 0.5 else \
            (rgb, light, 2 * t - 1)
        result.append(to_hex(a + (b - a) * u))
    return result
