# Example 12.6.2 (Figure 12.6): Observed counts of a uniform sample of 40 in seven bins, and the counts expected under $\mathcal{N}(0,1)$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

n_bins = 7
x = rng.uniform(-3, 3, size=40)

# observed and expected counts in each bin
edges = np.linspace(-3, 3, n_bins + 1)
observed, _ = np.histogram(x, bins=edges)
expected = x.size * np.diff(norm.cdf(edges))
# statistic and p-value (sf: one minus the cdf)
t_obs = np.sum((observed - expected)**2 / expected)
p_value = chi2.sf(t_obs, df=n_bins - 1)
print(f"T = {t_obs:.1f}, p-value = {p_value:.2g}")

centres = (edges[1:] + edges[:-1]) / 2
fig, ax = plt.subplots()
ax.bar(centres, observed, width=0.8, color=col.hist,
       label="observed")
ax.plot(centres, expected, "o", color=col.pmf,
        label="expected")
ax.set(xlabel="$x$", ylabel="counts")
ax.legend()

plt.show()
