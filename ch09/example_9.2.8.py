# Example 9.2.8 (Figure 9.5): Negative log-likelihood of $(\mu,\sigma^2)$ with the optimiser paths to the unrestricted and restricted ($\mu\leq1$) minima
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([1.1, 0.9, 1.4, 1.0, 1.2])


# the negative log-likelihood of (mu, sigma^2): the sum
# over the sample
def nll(mu, s2):
    total = 0
    for xi in x:
        total = total - norm.logpdf(xi, mu, np.sqrt(s2))
    return total


# the unrestricted minimum and the minimum with mu <= 1,
# both from the starting point (0.9, 0.25), with sigma^2
# kept positive; the path records each step
start = np.array([0.9, 0.25])
path_free = [start]
free = minimize(
    lambda p: nll(p[0], p[1]), start,
    bounds=[(None, None), (1e-9, None)],
    callback=lambda p: path_free.append(p.copy()))
path_restricted = [start]
restricted = minimize(
    lambda p: nll(p[0], p[1]), start,
    bounds=[(None, 1), (1e-9, None)],
    callback=lambda p: path_restricted.append(p.copy()))
path_free = np.array(path_free)
path_restricted = np.array(path_restricted)

# the test statistic: twice the difference of the minima
test = 2 * (restricted.fun - free.fun)
print(f"-2 log lambda(x) = {test:.3f}")

# the negative log-likelihood on a grid, for the background
mu_grid, s2_grid = np.meshgrid(np.linspace(0.8, 1.4, 101),
                               np.linspace(0.01, 0.3, 101))
fig, ax = plt.subplots()
ax.contourf(mu_grid, s2_grid, nll(mu_grid, s2_grid), 100,
            vmax=5, cmap="Purples_r")
ax.axvline(1, **ref)
ax.plot(path_free[:, 0], path_free[:, 1], "o-",
        color=col.path, ms=3, label="unrestricted")
ax.plot(path_restricted[:, 0], path_restricted[:, 1], "s--",
        color=col.path, ms=3, label=r"$\mu\leq1$")
ax.set_xlabel(r"$\mu$")
ax.set_ylabel(r"$\sigma^2$")
ax.legend()

plt.show()
