# Example 6.3.6 (Figure 6.9): Means of samples of size $n=1,5,30,100$ from $\mathrm{Exponential}(\beta=2)$ (top to bottom), and the normal pdf of the central limit theorem
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

trials = 100_000
sample_sizes = [1, 5, 30, 100]
beta = 2

fig, axes = plt.subplots(len(sample_sizes), 1)
for ax, n in zip(axes, sample_sizes):
    # the means of the samples of size n
    samples = rng.exponential(beta, size=(trials, n))
    means = samples.mean(axis=1)
    # the normal of the theorem, mean beta and variance
    # beta^2 / n, over four standard deviations
    sigma = beta / np.sqrt(n)
    lo = max(0, beta - 4 * sigma)
    hi = beta + 4 * sigma
    x = np.linspace(lo, hi, 200)
    ax.hist(means, bins=40, range=(lo, hi), density=True,
            color=col.hist)
    ax.plot(x, norm.pdf(x, beta, sigma), **ref)
    ax.set_title(f"$n={n}$")
    ax.set_xlabel("sample mean")
    ax.set_ylabel("density")

plt.show()
