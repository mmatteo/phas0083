# Thirty 90\% confidence intervals for $\mu$ from repeated samples of size 10: those that miss $\mu$ (dashed line) are in red
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

mu, sigma, n = 0, 1, 10
z = norm.ppf(0.95)
B = 30

fig, ax = plt.subplots()
missed = 0
for b in range(B):
    x = rng.normal(mu, sigma, n)
    half = z * sigma / np.sqrt(n)
    lo, hi = x.mean() - half, x.mean() + half
    covers = lo <= mu <= hi
    missed += not covers
    color = col.emp if covers else "#d62728"
    ax.plot([lo, hi], [b, b], color=color)
    ax.plot(x.mean(), b, "o", ms=2, color=col.data)
ax.axvline(mu, **ref)
ax.set_xlabel(r"$\bar{x} \pm 1.64\,\sigma/$√$n$")
ax.set_ylabel("sample")
ax.set_yticks([0, 10, 20, 29])
print(f"intervals missing mu: {missed} of {B}")

plt.show()
