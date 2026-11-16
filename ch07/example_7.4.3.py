# Example 7.4.3 (Figure 7.8): Distributions of the two estimators of $\sigma^2$ over the ensemble, with the true value
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

n = 5
sigma2 = 1.0
m = 100_000

# draw m samples of size n and compute both estimators
x = rng.normal(0, np.sqrt(sigma2), size=(m, n))
x_bar = x.mean(axis=1, keepdims=True)
sum_sq = np.sum((x - x_bar)**2, axis=1)
mle = sum_sq / n
S2 = sum_sq / (n - 1)

# compute bias, variance and mean squared error
print("       bias    var    mse")
for name, t in [("MLE", mle), ("S^2", S2)]:
    bias = t.mean() - sigma2
    var = t.var(ddof=1)
    mse = var + bias**2
    print(f"{name:4} {bias:6.3f}  {var:.3f}  {mse:.3f}")

dark, light = shades(col.draws, 2)
fig, ax = plt.subplots()
ax.hist(mle, bins=60, range=(0, 4), density=True,
        histtype="step", color=dark, lw=1.5,
        label=r"$\hat\sigma^2$")
ax.hist(S2, bins=60, range=(0, 4), density=True,
        histtype="step", color=light, lw=1.5, label="$S^2$")
ax.axvline(sigma2, color=col.ref, ls="--")
ax.set(xlabel=r"estimate of $\sigma^2$", ylabel="density")
ax.legend()

plt.show()
