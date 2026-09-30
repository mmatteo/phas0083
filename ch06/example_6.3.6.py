# Example 6.3.6 (Figure 6.11): Means of samples of size $n=1,2,5,30$ from $U(0,1)$ (top to bottom), and the normal pdf of the central limit theorem
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

trials = 1_000_000
sample_sizes = [1, 2, 5, 30]
u = np.linspace(0, 1, 200)

fig, axes = plt.subplots(len(sample_sizes), 1, sharex=True)
for ax, n in zip(axes, sample_sizes):
    samples = rng.uniform(0, 1, size=(trials, n))
    means = samples.mean(axis=1)
    sigma = np.sqrt(1 / (12 * n))
    ax.hist(means, bins=40, density=True, color=col.hist)
    ax.plot(u, norm.pdf(u, 0.5, sigma), **ref)
    ax.set_title(f"$n={n}$")
    ax.set_ylabel("density")
axes[-1].set_xlabel("sample mean")

plt.show()
