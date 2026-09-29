# Distribution of the p-value of a test of $\mu=0$ over 10000 samples: uniform under $H_0$ (top), piled up near zero under $H_1$ (bottom)
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

n, sigma = 10, 1
B = 10_000


def p_values(mu):
    """Two-sided p-values of the z test of mu = 0."""
    x = rng.normal(mu, sigma, (B, n))
    z = x.mean(axis=1) / (sigma / np.sqrt(n))
    return 2 * norm.sf(np.abs(z))


fig, axes = plt.subplots(2, 1, sharex=True)
labels = [r"$H_0$: $\mu=0$", r"$H_1$: $\mu=0.8$"]
for ax, mu, label in zip(axes, [0, 0.8], labels):
    p = p_values(mu)
    ax.hist(p, bins=20, range=(0, 1), density=True,
            color=col.hist)
    ax.axhline(1, **ref)
    ax.set_title(label)
    ax.set_ylabel("density")
    print(f"{label}: P(p < 0.05) = {np.mean(p < 0.05):.3f}")
axes[1].set_xlabel("p-value")

plt.show()
