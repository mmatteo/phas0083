# Likelihood of $\theta$ for the sample $\mathbf{x}$ with $\sigma=1$, at $\theta_0=1$ and at the MLE $\hat\theta$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([1.1, 0.9, 1.4, 1.0, 1.2])


def likelihood(mu, sigma=1):
    """Product of the normal pdfs; mu can be an array."""
    mu = np.array(mu).reshape(-1, 1)
    return np.prod(norm.pdf(x, mu, sigma), axis=1)


theta = np.linspace(0, 2, 200)
theta_0 = 1.0
theta_hat = x.mean()

fig, ax = plt.subplots()
ax.plot(theta, likelihood(theta), color=col.like)
marks = [(theta_0, ":", r"$\theta_0$"),
         (theta_hat, "-.", r"$\hat\theta$")]
for value, dash, label in marks:
    L = likelihood(value)
    ax.vlines(value, 0, L, color=col.thr, ls=dash,
              label=label)
    ax.hlines(L, 0, value, color=col.thr, ls=dash)
ax.set_xlabel(r"$\theta$")
ax.set_ylabel("likelihood")
ax.legend()

plt.show()
