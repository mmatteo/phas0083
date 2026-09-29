# Negative log-likelihood of $(\mu,\sigma^2)$ with the optimiser paths to the unrestricted and restricted ($\mu\leq1$) minima
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([1.1, 0.9, 1.4, 1.0, 1.2])


def nll(mu, s2):
    """Negative log-likelihood; mu and s2 can be arrays."""
    mu = np.atleast_1d(mu)[..., None]
    sigma = np.atleast_1d(np.sqrt(s2))[..., None]
    return -np.sum(norm.logpdf(x, mu, sigma), axis=-1)


def minimise(mu_max):
    """Minimise the NLL for mu <= mu_max."""
    path = [np.array([0.9, 0.25])]
    result = minimize(
        lambda p: nll(p[0], p[1]), x0=path[0],
        bounds=[(None, mu_max), (1e-9, None)],
        callback=lambda p: path.append(p.copy()))
    return result, np.array(path)


free, path_free = minimise(None)
restricted, path_restricted = minimise(1)
test = float(2 * (restricted.fun - free.fun))
print(f"-2 log lambda(x) = {test:.3f}")

mu_grid, s2_grid = np.meshgrid(np.linspace(0.8, 1.4, 101),
                               np.linspace(0.01, 0.3, 101))
fig, ax = plt.subplots()
ax.contourf(mu_grid, s2_grid, nll(mu_grid, s2_grid), 100,
            vmax=5, cmap="Purples_r")
ax.axvline(1, **ref)
ax.plot(*path_free.T, "o-", color=col.path, ms=3,
        label="unrestricted")
ax.plot(*path_restricted.T, "s--", color=col.path, ms=3,
        label=r"$\mu\leq1$")
ax.set_title(rf"$-2\log\lambda(\mathbf{{x}})={test:.3f}$")
ax.set_xlabel(r"$\mu$")
ax.set_ylabel(r"$\sigma^2$")
ax.legend()

plt.show()
