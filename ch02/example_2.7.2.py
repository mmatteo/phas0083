# Example 2.7.2 (Figure 2.11): Pdf of the standard normal distribution, and the probability within 1, 2 and 3 standard deviations of the mean
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

k = np.array([1, 2, 3])
p = norm.cdf(k) - norm.cdf(-k)
for k_i, p_i in zip(k, p):
    print(f"P(|X| < {k_i}) = {p_i:.4f}")

x = np.linspace(-4, 4, 400)
fig, ax = plt.subplots()
ax.plot(x, norm.pdf(x), color=col.pdf)
for edge in np.concatenate([-k, k]):
    ax.axvline(edge, color=col.ref, ls=":")
ax.set(xlabel="$x$", ylabel="$f_X(x)$")

plt.show()
