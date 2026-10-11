# Example A.2.2 (Figure A.2): Negative log-likelihood of the two-run model for $x=14$, $y=18$ and $\tau=2$, above its minimum, with the maximum likelihood estimates
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

def nll(lam, nu, x, y, tau):
    """Negative log-likelihood of the two-run model."""
    return ((lam + nu) - x * np.log(lam + nu)
            + tau * nu - y * np.log(tau * nu))


x, y, tau = 14, 18, 2.0
lam_hat, nu_hat = max(0, x - y / tau), y / tau
print(f"MLEs: lambda {lam_hat:.1f}, nu {nu_hat:.1f}")

lam, nu = np.meshgrid(np.linspace(0, 14, 200),
                      np.linspace(4, 16, 200))
z = nll(lam, nu, x, y, tau)
z -= nll(lam_hat, nu_hat, x, y, tau)

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
