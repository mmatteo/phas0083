# Example 4.3.4 (Figure 4.11): Error of the estimated $P(-1<X<1)$ against $N$ in four independent repetitions, and the predicted binomial precision
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

p_true = norm.cdf(1) - norm.cdf(-1)
N_values = np.array([10, 100, 1000, 10**4, 10**5, 10**6])

# repeat the estimate four times at each N
fig, ax = plt.subplots()
for color in shades(col.draws, 4):
    err = []
    for N in N_values:
        x = rng.normal(0, 1, size=N)
        p_hat = np.mean(np.abs(x) < 1)
        err.append(np.abs(p_hat - p_true))
    ax.loglog(N_values, err, "o-", color=color)

# predicted precision
sd = np.sqrt(p_true * (1 - p_true) / N_values)
ax.loglog(N_values, sd, color=col.ref, ls="--",
          label=r"$\sqrt{p(1-p)/N}$")
ax.set(xlabel="$N$", ylabel=r"$|\hat{p} - p|$")
ax.legend()

plt.show()
