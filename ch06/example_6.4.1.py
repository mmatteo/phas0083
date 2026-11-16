# Example 6.4.1 (Figure 6.12): Sample mean (top) and sample variance (bottom) over an ensemble of $10^5$ simulated samples of size $n=5$ from $\mathcal{N}(3.3,0.25)$, with the normal $\mathcal{N}(\mu,\sigma^2/n)$ and the value of $\sigma^2$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

m = 100_000
n = 5
mu = 3.3
sigma = 0.5

# draw m samples of size n, one per row
x = rng.normal(mu, sigma, size=(m, n))

# compute the mean and variance of each sample
x_bar = x.mean(axis=1)
S2 = x.var(axis=1, ddof=1)

print(f"mean of x_bar: {x_bar.mean():.3f} (mu = {mu})")
print(f"var of x_bar: {x_bar.var(ddof=1):.4f} "
      f"({sigma**2 / n})")
print(f"mean of S2: {S2.mean():.3f} (sigma^2 = {sigma**2})")

u = np.linspace(mu - 2 * sigma, mu + 2 * sigma, 200)
pdf = norm.pdf(u, mu, sigma / np.sqrt(n))
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.hist(x_bar, bins=50, density=True, color=col.hist)
ax1.plot(u, pdf, color=col.ref, ls="--")
ax1.set_xlabel(r"sample mean $\bar{x}$ [ns]")
ax2.hist(S2, bins=50, density=True, color=col.hist)
ax2.axvline(sigma**2, color=col.ref, ls="--")
ax2.set_xlabel(r"sample variance $S^2$ [ns$^2$]")
plt.setp((ax1, ax2), ylabel="density")

plt.show()
