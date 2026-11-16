# Example 9.1.5 (Figure 9.2): One hundred intervals $[\bar{x}-1,\bar{x}+1]$ for $\mu$ from repeated samples of size 4: those that miss $\mu$ (dashed line) are in red
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

mu = 0
sigma = 1
n = 4
m = 100

# draw m samples of size n and compute their means
x = rng.normal(mu, sigma, size=(m, n))
x_bar = x.mean(axis=1)
missed = np.abs(x_bar - mu) > 1
print(f"intervals missing mu: {missed.sum()} of {m}")

# colour in red the intervals that miss mu
colors = np.where(missed, "tab:red", col.draws)
sample = np.arange(m)
fig, ax = plt.subplots()
ax.hlines(sample, x_bar - 1, x_bar + 1, colors=colors)
ax.plot(x_bar, sample, "o", color=col.data, ms=2)
ax.axvline(mu, color=col.ref, ls="--")
ax.set(xlabel=r"$\bar{x} \pm 1$", ylabel="sample")

plt.show()
