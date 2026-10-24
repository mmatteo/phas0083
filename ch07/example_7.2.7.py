# Example 7.2.7 (Figure 7.7): Likelihood of $(\mu,\sigma^2)$ for the sample $\mathbf{x}$ of a normal population
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([1.1, 0.9, 1.4, 1.0, 1.2])
mu_grid, s2_grid = np.meshgrid(np.linspace(0.8, 1.4, 101),
                               np.linspace(0.01, 0.3, 101))

# likelihood on the grid: the product of the pdfs of the x_i
L = 1
for xi in x:
    L = L * norm.pdf(xi, mu_grid, np.sqrt(s2_grid))

# the grid point of the maximum
best = L == L.max()
print(f"maximum at mu = {mu_grid[best][0]:.3f},"
      f" sigma^2 = {s2_grid[best][0]:.4f}")

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
