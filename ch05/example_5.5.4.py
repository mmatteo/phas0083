# Example 5.5.4 (Figure 5.17): Running variance of $R=X/Y$ for $N$ up to $2\times10^6$ draws, and the delta-method value
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

mu_X, sd_X = 10.0, 1.0
mu_Y, sd_Y = 3.0, 1.0   # 3 standard deviations from 0

dR_dX = 1 / mu_Y
dR_dY = -mu_X / mu_Y**2
var_delta = dR_dX**2 * sd_X**2 + dR_dY**2 * sd_Y**2
print(f"delta method: Var(R) ~ {var_delta:.3f}")

rng = np.random.default_rng(7)
N = 2_000_000
X = rng.normal(mu_X, sd_X, N)
Y = rng.normal(mu_Y, sd_Y, N)
R = X / Y

steps = np.logspace(3, np.log10(N), 40).astype(int)
steps = np.unique(steps)
running_var = [np.var(R[:n], ddof=1) for n in steps]

fig, ax = plt.subplots()
ax.plot(steps, running_var, "o-", color=col.emp)
ax.axhline(var_delta, **ref, label="delta method")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("$N$")
ax.set_ylabel("running Var$(R)$")
ax.legend()

plt.show()
