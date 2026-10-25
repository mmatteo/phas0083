# Example 7.2.8 (Figure 7.6): Negative log-likelihood of $(\mu,\sigma^2)$ and the path of the optimiser to its minimum
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([1.1, 0.9, 1.4, 1.0, 1.2])


def nll(theta):
    mu, s2 = theta
    return -np.sum(norm.logpdf(x, mu, np.sqrt(s2)))


# the minimum, from the starting point (1.0, 0.3), with
# sigma^2 kept positive; the path records each step
path = []
result = minimize(nll, [1.0, 0.3],
                  bounds=[(None, None), (1e-9, None)],
                  callback=path.append)
path = np.array(path)
mu_hat, s2_hat = result.x
print(f"minimum at mu = {mu_hat:.3f}")
print(f"           sigma^2 = {s2_hat:.4f}")

# the negative log-likelihood on a grid, for the background,
# in one call: the sample as a column, with one axis for the
# sample and two for the grid, summed over the sample
mu_grid, s2_grid = np.meshgrid(np.linspace(0.8, 1.4, 101),
                               np.linspace(0.01, 0.3, 101))
nll_grid = -np.sum(norm.logpdf(x[:, None, None], mu_grid,
                               np.sqrt(s2_grid)), axis=0)

fig, ax = plt.subplots()
contour = ax.contourf(mu_grid, s2_grid, nll_grid, 100,
                      vmax=5, cmap="Purples_r")
bar = fig.colorbar(contour, ax=ax, location="top",
                   label="neg. log-likelihood")
bar.locator = plt.MaxNLocator(4)
bar.update_ticks()
ax.plot(path[:, 0], path[:, 1], "o-", color=col.path, ms=3)
ax.set_xlabel(r"$\mu$")
ax.set_ylabel(r"$\sigma^2$")

plt.show()
