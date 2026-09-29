# Negative log-likelihood of $(\mu,\sigma^2)$ and the path of the optimiser to its minimum
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([1.1, 0.9, 1.4, 1.0, 1.2])


def nll(mu, s2):
    """Negative log-likelihood; mu and s2 can be arrays."""
    sigma = np.sqrt(s2)[..., None]
    logpdf = norm.logpdf(x, mu[..., None], sigma)
    return -np.sum(logpdf, axis=-1)


mu_grid, s2_grid = np.meshgrid(np.linspace(0.8, 1.4, 101),
                               np.linspace(0.01, 0.3, 101))

path = []
result = minimize(lambda p: nll(p[0], p[1]), [1.0, 0.3],
                  bounds=[(None, None), (1e-9, None)],
                  callback=lambda p: path.append(p.copy()))
path = np.array(path)
mu_hat, s2_hat = result.x
print(f"minimum at mu = {mu_hat:.3f},"
      f" sigma^2 = {s2_hat:.4f}")

fig, ax = plt.subplots()
nll_grid = nll(mu_grid, s2_grid)
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
