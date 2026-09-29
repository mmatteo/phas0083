# Error of the estimated $P(-1<X<1)$ against $N$ in four runs, and the predicted binomial precision
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

p_true = norm.cdf(1) - norm.cdf(-1)   # P(-1 < X < 1)
N_values = np.array([10, 30, 100, 300, 1000, 3000,
                     1e4, 3e4, 1e5, 3e5, 1e6], dtype=int)

fig, ax = plt.subplots()
for color in shades(col.emp, 4):  # four independent runs
    x = rng.normal(0, 1, N_values[-1])
    inside = np.abs(x) < 1
    p_hat = np.cumsum(inside)[N_values - 1] / N_values
    ax.plot(N_values, np.abs(p_hat - p_true), "o-",
            color=color)

# binomial precision: std of the estimate, sqrt(p(1-p)/N)
sd = np.sqrt(p_true * (1 - p_true) / N_values)
ax.plot(N_values, sd, **ref, label=r"$\sqrt{p(1-p)/N}$")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("$N$")
ax.set_ylabel(r"$|\hat{F}_N - p|$")
ax.legend()

plt.show()
