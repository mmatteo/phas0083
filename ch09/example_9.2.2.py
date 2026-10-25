# Example 9.2.2 (Figure 9.3): Likelihood of $\theta$ for the sample $\mathbf{x}$ with $\sigma=1$, at $\theta_0=1$ and at the MLE $\hat\theta$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([1.1, 0.9, 1.4, 1.0, 1.2])
sigma = 1


# the likelihood of mu: the product of the pdfs of the x_i
def likelihood(mu):
    L = 1
    for xi in x:
        L = L * norm.pdf(xi, mu, sigma)
    return L


theta = np.linspace(0, 2, 200)
theta_0 = 1.0
theta_hat = x.mean()

fig, ax = plt.subplots()
ax.plot(theta, likelihood(theta), color=col.like)
# the likelihood at theta_0 and at the MLE
L_0 = likelihood(theta_0)
L_hat = likelihood(theta_hat)
ax.vlines(theta_0, 0, L_0, color=col.thr, ls=":",
          label=r"$\theta_0$")
ax.hlines(L_0, 0, theta_0, color=col.thr, ls=":")
ax.vlines(theta_hat, 0, L_hat, color=col.thr, ls="-.",
          label=r"$\hat\theta$")
ax.hlines(L_hat, 0, theta_hat, color=col.thr, ls="-.")
ax.set_xlabel(r"$\theta$")
ax.set_ylabel("likelihood")
ax.legend()

plt.show()
