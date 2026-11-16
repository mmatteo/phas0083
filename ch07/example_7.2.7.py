# Example 7.2.7 (Figure 7.5): Likelihood of $(\mu,\sigma^2)$ for the sample $\mathbf{x}$ of a normal population
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
i, j = np.unravel_index(np.argmax(L), L.shape)
print(f"maximum: mu = {mu_grid[i, j]:.3f}")
print(f"sigma^2 = {s2_grid[i, j]:.4f}")

fig, ax = plt.subplots()
contour = ax.contourf(mu_grid, s2_grid, L, levels=30,
                      cmap="Purples")
fig.colorbar(contour, label="likelihood", location="top",
             ticks=MaxNLocator(4))
ax.set(xlabel=r"$\mu$", ylabel=r"$\sigma^2$")

plt.show()
