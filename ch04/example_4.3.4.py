# Example 4.3.4 (Figure 4.9): Error of the estimated $P(-1<X<1)$ against $N$ in four independent repetitions, and the predicted binomial precision
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

p_true = norm.cdf(1) - norm.cdf(-1)   # P(-1 < X < 1)
N_values = np.array([10, 30, 100, 300, 1000, 3000,
                     1e4, 3e4, 1e5, 3e5, 1e6], dtype=int)

N_max = N_values[-1]

fig, ax = plt.subplots()
for color in shades(col.emp, 4):  # four repetitions
    x = rng.normal(0, 1, N_max)         # one simulation
    below = np.cumsum(np.abs(x) < 1)    # count so far
    p_hat = below[N_values - 1] / N_values   # after N draws
    ax.plot(N_values, np.abs(p_hat - p_true), "o-",
            color=color)

# binomial precision: std of the estimate, sqrt(p(1-p)/N)
sd = np.sqrt(p_true * (1 - p_true) / N_values)
ax.plot(N_values, sd, **ref, label=r"√$(p(1-p)/N)$")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("$N$")
ax.set_ylabel(r"$|\hat{p} - p|$")
ax.legend()

plt.show()
