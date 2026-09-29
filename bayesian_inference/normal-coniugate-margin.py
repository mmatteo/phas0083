# Prior $\mathcal{N}(0,1)$, likelihood of the observation $y=2$ with $\sigma=1$, and posterior of $\theta$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

mu_0, tau_0 = 0.0, 1.0   # prior
sigma, y = 1.0, 2.0      # observation

precision = 1 / tau_0**2 + 1 / sigma**2
mu_1 = (mu_0 / tau_0**2 + y / sigma**2) / precision
tau_1 = np.sqrt(1 / precision)

theta = np.linspace(mu_0 - 4 * tau_0, y + 4 * sigma, 500)
fig, ax = plt.subplots()
ax.plot(theta, norm.pdf(theta, mu_0, tau_0), color=col.hist,
        label="prior")
ax.plot(theta, norm.pdf(theta, y, sigma), color=col.like,
        label="likelihood")
ax.plot(theta, norm.pdf(theta, mu_1, tau_1), color=col.pdf,
        label="posterior")
ax.set_xlabel(r"$\theta$")
ax.set_ylabel("density")
ax.legend()

plt.show()
