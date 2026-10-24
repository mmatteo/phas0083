# Example 4.3.4 (Figure 4.10): Error of the estimated $P(-1<X<1)$ against $N$ in four independent repetitions, and the predicted binomial precision
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

p_true = norm.cdf(1) - norm.cdf(-1)   # P(-1 < X < 1)
N_values = np.array([10, 100, 1000, 10**4, 10**5, 10**6])
N_max = N_values[-1]

fig, ax = plt.subplots()
# four repetitions, one simulation of N_max draws each; the
# estimate after N draws comes from the running count
for color in shades(col.emp, 4):
    x = rng.normal(0, 1, N_max)
    below = np.cumsum(np.abs(x) < 1)
    p_hat = below[N_values - 1] / N_values
    err = abs(p_hat - p_true)
    ax.loglog(N_values, err, "o-", color=color)

# the predicted precision, sqrt(p(1-p)/N)
sd = np.sqrt(p_true * (1 - p_true) / N_values)
ax.loglog(N_values, sd, **ref, label=r"√$(p(1-p)/N)$")
ax.set(xlabel="$N$", ylabel=r"$|\hat{p} - p|$")
ax.legend()

plt.show()
