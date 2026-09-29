# Simulated velocity $V=D/T$ and the normal pdf predicted by the delta method
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

mu_T, sd_T = 10.0, 1.0   # T ~ N(mu_T, sd_T^2), seconds
a, b = 99.0, 101.0       # D ~ Uniform(a, b), centimetres


def f_joint(d, t):
    """Joint pdf of (D, T): independent, so the product."""
    return norm.pdf(t, mu_T, sd_T) / (b - a)


# exact moments, by 2D numerical integration
E_V, _ = integrate.dblquad(
    lambda d, t: (d / t) * f_joint(d, t), 1, 30, a, b)
E_V2, _ = integrate.dblquad(
    lambda d, t: (d / t)**2 * f_joint(d, t), 1, 30, a, b)
var_exact = E_V2 - E_V**2

# delta method
mu_D, var_D = (a + b) / 2, (b - a)**2 / 12
dV_dT, dV_dD = -mu_D / mu_T**2, 1 / mu_T
var_delta = dV_dT**2 * sd_T**2 + dV_dD**2 * var_D

# simulation
N = 2_000_000
T = rng.normal(mu_T, sd_T, N)
D = rng.uniform(a, b, N)
V = D / T

print("            E[V]    Var[V]")
print(f"exact      {E_V:.3f}  {var_exact:.3f}")
print(f"delta      {mu_D / mu_T:.3f}  {var_delta:.3f}")
print(f"simulated  {V.mean():.3f}  {V.var(ddof=1):.3f}")

u = np.linspace(7, 14, 200)
fig, ax = plt.subplots()
ax.hist(V, bins=60, density=True, range=(7, 14),
        color=col.hist, label="simulation")
ax.plot(u, norm.pdf(u, mu_D / mu_T, var_delta**0.5),
        **ref, label="delta method")
ax.set_xlabel("$V$ [cm/s]")
ax.set_ylabel("density")
ax.legend()

plt.show()
