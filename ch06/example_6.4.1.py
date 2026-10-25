# Example 6.4.1 (Figure 6.10): Sample mean (top) and sample variance (bottom) over an ensemble of $10^5$ simulated samples of size $n=5$ from $\mathcal{N}(2.0,0.25)$, with the normal $\mathcal{N}(\mu,\sigma^2/n)$ and the value of $\sigma^2$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

trials = 100_000
n = 5
mu = 2.0
sigma = 0.5

# the ensemble: one simulated sample per row
x = rng.normal(mu, sigma, size=(trials, n))

# the two statistics of every sample: the sample mean, the
# sample variance (n - 1) and the sum of squares over n
x_bar = x.mean(axis=1)
S2 = x.var(axis=1, ddof=1)
s2_n = x.var(axis=1)

# their means and variances over the ensemble
print(f"mean of x_bar: {x_bar.mean():.3f} (mu = {mu})")
print(f"var of x_bar: {x_bar.var():.4f} ({sigma**2 / n})")
print(f"mean of S2: {S2.mean():.3f} (s^2 = {sigma**2})")
print(f"mean of sum of squares / n: {s2_n.mean():.3f}")

fig, (ax1, ax2) = plt.subplots(2, 1)
t = np.linspace(1, 3, 200)
ax1.hist(x_bar, bins=50, density=True, color=col.hist)
ax1.plot(t, norm.pdf(t, mu, sigma / np.sqrt(n)), **ref)
ax1.set_xlabel(r"sample mean $\bar{x}$ [ns]")
ax1.set_ylabel("density")
ax2.hist(S2, bins=50, density=True, color=col.hist)
ax2.axvline(sigma**2, **thr)
ax2.set_xlabel(r"sample variance $S^2$ [ns$^2$]")
ax2.set_ylabel("density")

plt.show()
