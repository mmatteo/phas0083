# Example 7.4.3 (Figure 7.8): Distributions of the two estimators of $\sigma^2$ over the ensemble, with the true value
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

n = 5
sigma2 = 1.0
N = 100_000

# the ensemble of simulated samples, and the two estimators
# of sigma^2 on each: the MLE divides by n, S^2 by n - 1
x = rng.normal(0, np.sqrt(sigma2), size=(N, n))
x_bar = x.mean(axis=1, keepdims=True)
sum_sq = np.sum((x - x_bar)**2, axis=1)
mle = sum_sq / n
S2 = sum_sq / (n - 1)

# bias, variance and mean squared error over the ensemble
print("       bias    var    mse")
for name, t in [("MLE", mle), ("S^2", S2)]:
    bias = t.mean() - sigma2
    var = t.var(ddof=1)
    mse = var + bias**2
    print(f"{name:4} {bias:6.3f}  {var:.3f}  {mse:.3f}")

fig, ax = plt.subplots()
dark, light = shades(col.emp, 2)
ax.hist(mle, bins=60, range=(0, 4), density=True,
        histtype="step", color=dark,
        label=r"$\hat\sigma^2$")
ax.hist(S2, bins=60, range=(0, 4), density=True,
        histtype="step", color=light, label="$S^2$")
ax.axvline(sigma2, **ref)
ax.set_xlabel("estimate of $\\sigma^2$")
ax.set_ylabel("density")
ax.legend()

plt.show()
