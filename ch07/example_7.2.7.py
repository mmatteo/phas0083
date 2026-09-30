# Example 7.2.7 (Figure 7.7): Likelihood of $(\mu,\sigma^2)$ for the sample $\mathbf{x}$ of a normal population
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([1.1, 0.9, 1.4, 1.0, 1.2])


def likelihood(mu, s2):
    """Product of the normal pdfs of the sample values."""
    sigma = np.sqrt(s2)
    pdf = [norm.pdf(xi, mu, sigma) for xi in x]
    return np.prod(pdf, axis=0)


mu_grid, s2_grid = np.meshgrid(np.linspace(0.8, 1.4, 101),
                               np.linspace(0.01, 0.3, 101))
L = likelihood(mu_grid, s2_grid)
i_max = np.unravel_index(np.argmax(L), L.shape)
print(f"maximum at mu = {mu_grid[i_max]:.3f},"
      f" sigma^2 = {s2_grid[i_max]:.4f}")

fig, ax = plt.subplots()
contour = ax.contourf(mu_grid, s2_grid, L, levels=30,
                      cmap="Purples")
bar = fig.colorbar(contour, ax=ax, location="top",
                   label="likelihood")
bar.locator = plt.MaxNLocator(4)
bar.update_ticks()
ax.set_xlabel(r"$\mu$")
ax.set_ylabel(r"$\sigma^2$")

plt.show()
