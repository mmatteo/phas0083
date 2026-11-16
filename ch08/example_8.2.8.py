# Example 8.2.8 (Figure 8.5): Negative log-likelihood of $(\mu,\sigma^2)$ with the optimiser paths to the unrestricted and restricted ($\mu\leq1$) minima
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([1.1, 0.9, 1.4, 1.0, 1.2])


def nll(theta):
    mu, s2 = theta
    return -np.sum(norm.logpdf(x, mu, np.sqrt(s2)))


# minimise nll from start, without and with mu <= 1
start = [0.9, 0.25]
path_free = [start]
result_free = minimize(
    nll, start, bounds=[(None, None), (1e-9, None)],
    callback=path_free.append)
path_0 = [start]
result_0 = minimize(
    nll, start, bounds=[(None, 1), (1e-9, None)],
    callback=path_0.append)
path_free = np.array(path_free)
path_0 = np.array(path_0)

# the test statistic: twice the difference of the minima
t_obs = 2 * (result_0.fun - result_free.fun)
print(f"-2 log lambda(x) = {t_obs:.3f}")

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
ax.axvline(1, color=col.ref, ls="--")
ax.plot(path_free[:, 0], path_free[:, 1], "o-",
        color="tab:orange", ms=3, label="unrestricted")
ax.plot(path_0[:, 0], path_0[:, 1], "s-",
        color="tab:orange", ms=3, label=r"$\mu\leq1$")
ax.set(xlabel=r"$\mu$", ylabel=r"$\sigma^2$")
ax.legend()

plt.show()
