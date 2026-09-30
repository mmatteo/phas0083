# Example 12.6.2 (Figure 12.6): Observed counts of a uniform sample of 40 in seven bins, and the counts expected under $\mathcal{N}(0,1)$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

n_bins = 7
x = rng.uniform(-3, 3, size=40)

edges = np.linspace(-3, 3, n_bins)
O, _ = np.histogram(x, bins=edges)  # noqa: E741
E = x.size * np.diff(norm.cdf(edges))
T = np.sum((O - E)**2 / E)
p_value = 1 - chi2.cdf(T, n_bins - 1)
print(f"T = {T:.1f}, p-value = {p_value:.2g}")

centres = (edges[1:] + edges[:-1]) / 2
fig, ax = plt.subplots()
ax.bar(centres, O, width=0.9, color=col.hist,
       label="observed")
ax.plot(centres, E, "o", color=col.ref, label="expected")
ax.set_xlabel("$x$")
ax.set_ylabel("counts")
ax.legend()

plt.show()
