# Example A.2.2 (Figure A.2): Negative log-likelihood of the two-run model for $x=14$, $y=18$ and $\tau=2$, above its minimum, with the maximum likelihood estimates
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

# the negative log-likelihood of the two-run model, up to
# constant terms
def nll(lam, nu, x, y, tau):
    return ((lam + nu) - x * np.log(lam + nu)
            + tau * nu - y * np.log(tau * nu))


x = 14
y = 18
tau = 2.0
# the MLEs, with lambda kept at or above zero
lam_hat = max(0, x - y / tau)
nu_hat = y / tau
print(f"MLEs: lambda {lam_hat:.1f}, nu {nu_hat:.1f}")

# the negative log-likelihood above its minimum on a grid
lam, nu = np.meshgrid(np.linspace(0, 14, 200),
                      np.linspace(4, 16, 200))
z = (nll(lam, nu, x, y, tau)
     - nll(lam_hat, nu_hat, x, y, tau))

fig, ax = plt.subplots()
cs = ax.contour(lam, nu, z, levels=[0.5, 2, 4.5],
                colors=col.like)
ax.clabel(cs, fmt="%.1f")
ax.plot(lam_hat, nu_hat, "*", color=col.data, ms=8,
        label="MLE")
ax.set_xlabel(r"$\lambda$")
ax.set_ylabel(r"$\nu$")
ax.legend()

plt.show()
