# Example 8.5.2 (Figure 8.10): Power of the level-0.05 test as a function of the signal $\lambda$, with the background known
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

# -2 log of the likelihood ratio for H0: lambda = 0, with
# the background nu known and the MLE of lambda kept at
# or above zero
def nlrt(x, nu):
    lambda_hat = np.maximum(0, x - nu)
    return (-2 * poisson.logpmf(x, nu)
            + 2 * poisson.logpmf(x, lambda_hat + nu))


nu = 50
m = 10_000

# the threshold of the previous example
c = 2.674

# the power at each lambda: the fraction of the simulated
# counts that the test rejects
lam_values = np.linspace(0, 30, 20)
power = []
for lam in lam_values:
    x = rng.poisson(lam + nu, size=m)
    power.append(np.mean(nlrt(x, nu) > c))

fig, ax = plt.subplots()
ax.plot(lam_values, power, "o-", color=col.emp)
ax.set_xlabel(r"$\lambda$")
ax.set_ylabel("power")

plt.show()
