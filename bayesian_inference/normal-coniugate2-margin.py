# Four sequential updates of a normal prior (top to bottom), each posterior becoming the next prior
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

mu, tau = 0.0, 1.0   # initial prior
sigma = 1.0
observations = [2.0, 1.5, 3.0, 2.2]
theta = np.linspace(-2, 4, 400)

fig, axes = plt.subplots(len(observations), 1, sharex=True)
for i, (ax, y) in enumerate(zip(axes, observations), 1):
    precision = 1 / tau**2 + 1 / sigma**2
    mu_new = (mu / tau**2 + y / sigma**2) / precision
    tau_new = np.sqrt(1 / precision)
    ax.plot(theta, norm.pdf(theta, mu, tau), color=col.hist,
            label="prior")
    ax.plot(theta, norm.pdf(theta, y, sigma),
            color=col.like, label="likelihood")
    ax.plot(theta, norm.pdf(theta, mu_new, tau_new),
            color=col.pdf,
            label="posterior")
    ax.set_title(f"update {i}: $y={y}$")
    ax.set_ylabel("density")
    mu, tau = mu_new, tau_new
axes[-1].set_xlabel(r"$\theta$")
axes[0].legend()

plt.show()
