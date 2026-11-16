# Example 10.3.3 (Figure 10.9): Sample of 60 values from the peak-over-background model, with $\hat\mu$ and its 90\% confidence interval
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

sigma = 1.0
alpha = 0.10
x = np.concatenate([rng.normal(0.5, sigma, size=40),
                    rng.uniform(-4, 4, size=20)])


def nlrt(mu_0):
    return x.size * ((x.mean() - mu_0) / sigma)**2


# interval: mu_0 below the chi-squared threshold
mu_hat = x.mean()
mu_grid = np.linspace(mu_hat - 3, mu_hat + 3, 1000)
c = chi2.ppf(1 - alpha, df=1)
inside = mu_grid[nlrt(mu_grid) <= c]
low = inside.min()
high = inside.max()
print(f"mu_hat = {mu_hat:.2f}, I = [{low:.2f}, {high:.2f}]")

fig, ax = plt.subplots()
ax.hist(x, bins=20, color=col.hist)
ax.axvline(mu_hat, color=col.data, label=r"$\hat\mu$")
ax.axvline(low, color=col.ref, ls=":", label="$I$")
ax.axvline(high, color=col.ref, ls=":")
ax.set(xlabel="$x$", ylabel="counts")
ax.legend()

plt.show()
