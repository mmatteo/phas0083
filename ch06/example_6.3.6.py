# Example 6.3.6 (Figure 6.11): Means of samples of size $n=1,5,30,100$ from $\mathrm{Exponential}(\beta=2)$ (top to bottom), and the normal pdf of the central limit theorem
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

m = 100_000
sample_sizes = [1, 5, 30, 100]
beta = 2

fig, axes = plt.subplots(len(sample_sizes), 1)
for ax, n in zip(axes, sample_sizes):
    # draw m samples of size n and compute their means
    x = rng.exponential(scale=beta, size=(m, n))
    x_bar = x.mean(axis=1)
    # plot range: four standard deviations around beta
    sigma = beta / np.sqrt(n)
    lo = max(0, beta - 4 * sigma)
    hi = beta + 4 * sigma
    u = np.linspace(lo, hi, 200)
    ax.hist(x_bar, bins=40, range=(lo, hi), density=True,
            color=col.hist)
    ax.plot(u, norm.pdf(u, beta, sigma), color=col.ref,
            ls="--")
    ax.set_title(f"$n={n}$")
plt.setp(axes, xlabel="sample mean", ylabel="density")

plt.show()
