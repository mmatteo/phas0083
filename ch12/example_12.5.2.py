# Example 12.5.2 (Figure 12.5): Empirical cdf of a uniform sample of 20 and the cdf of the normal model tested by Kolmogorov--Smirnov
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = rng.uniform(-3, 3, size=20)
ks = stats.kstest(x, norm.cdf)
print(f"D = {ks.statistic:.3f}, p-value = {ks.pvalue:.1g}")

u = np.linspace(-3, 3, 100)
fig, ax = plt.subplots()
ax.ecdf(x, color=col.emp, label="data")
ax.plot(u, norm.cdf(u), color=col.cdf, label="model")
ax.plot(x, np.zeros_like(x), "|", color=col.data, ms=8)
ax.set_xlabel("$x$")
ax.set_ylabel("cdf")
ax.legend()

plt.show()
