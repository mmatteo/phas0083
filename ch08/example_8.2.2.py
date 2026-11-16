# Example 8.2.2 (Figure 8.3): Likelihood of $\theta$ for the sample $\mathbf{x}$ with $\sigma=1$, at $\theta_0=1$ and at the MLE $\hat\theta$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([1.1, 0.9, 1.4, 1.0, 1.2])
sigma = 1
theta_0 = 1.0


def likelihood(mu):
    # broadcasting: x[:, None] makes x a column, so mu
    # can be an array
    return np.prod(norm.pdf(x[:, None], mu, sigma), axis=0)


# the likelihood at theta_0 and at the MLE
theta_hat = x.mean()
L_0, L_hat = likelihood([theta_0, theta_hat])

theta = np.linspace(0, 2, 200)
fig, ax = plt.subplots()
ax.plot(theta, likelihood(theta), color=col.like)
ax.vlines(theta_0, 0, L_0, color=col.ref, ls=":",
          label=r"$\theta_0$")
ax.hlines(L_0, theta[0], theta_0, color=col.ref, ls=":")
ax.vlines(theta_hat, 0, L_hat, color=col.data,
          label=r"$\hat\theta$")
ax.hlines(L_hat, theta[0], theta_hat, color=col.data)
ax.set(xlabel=r"$\theta$", ylabel="likelihood")
ax.legend()

plt.show()
