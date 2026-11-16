# Example 7.2.8 (Figure 7.6): Negative log-likelihood of $(\mu,\sigma^2)$ and the path of the optimiser to its minimum
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([1.1, 0.9, 1.4, 1.0, 1.2])


def nll(theta):
    mu, s2 = theta
    return -np.sum(norm.logpdf(x, mu, np.sqrt(s2)))


# minimise nll from start, within bounds (sigma^2 > 0)
start = [0.85, 0.25]
path = [start]
result = minimize(nll, start,
                  bounds=[(None, None), (1e-9, None)],
                  callback=path.append)
path = np.array(path)
mu_hat, s2_hat = result.x
print(f"minimum: mu = {mu_hat:.3f}")
print(f"sigma^2 = {s2_hat:.4f}")

# compute the negative log-likelihood on a grid
mu_grid, s2_grid = np.meshgrid(np.linspace(0.8, 1.4, 101),
                               np.linspace(0.01, 0.3, 101))
# broadcasting: x[:, None, None] puts x on its own axis
nll_grid = -np.sum(norm.logpdf(x[:, None, None], mu_grid,
                               np.sqrt(s2_grid)), axis=0)

fig, ax = plt.subplots()
contour = ax.contourf(mu_grid, s2_grid, nll_grid,
                      levels=100, vmax=5, cmap="Purples_r")
fig.colorbar(contour, label="neg. log-likelihood",
             location="top", ticks=MaxNLocator(4))
ax.plot(path[:, 0], path[:, 1], "o-", color="tab:orange",
        ms=3)
ax.set(xlabel=r"$\mu$", ylabel=r"$\sigma^2$")

plt.show()
