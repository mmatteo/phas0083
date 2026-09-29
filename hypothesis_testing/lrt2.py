# Likelihood of $\mu$ with $\sigma^2$ at its restricted and unrestricted MLEs, and the resulting likelihood ratio
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([1.1, 0.9, 1.4, 1.0, 1.2])


def likelihood(mu, s2):
    """Product of the normal pdfs; mu can be an array."""
    mu = np.array(mu).reshape(-1, 1)
    return np.prod(norm.pdf(x, mu, np.sqrt(s2)), axis=1)


mu_0 = min(1.0, x.mean())        # MLE under H0: mu <= 1
s2_0 = np.mean((x - mu_0)**2)
mu_hat = x.mean()                # unrestricted MLE
s2_hat = np.mean((x - mu_hat)**2)
L_0 = likelihood(mu_0, s2_0)[0]
L_hat = likelihood(mu_hat, s2_hat)[0]
ratio = L_0 / L_hat

mu = np.linspace(0.8, 1.4, 200)
cases = [(mu_0, s2_0, ":", r"$\hat\sigma_0^2$"),
         (mu_hat, s2_hat, "-.", r"$\hat\sigma^2$")]
fig, ax = plt.subplots()
for color, (m, s2, dash, label) in zip(shades(col.like, 2),
                                       cases):
    ax.plot(mu, likelihood(mu, s2), color=color,
            label=label)
    L = likelihood(m, s2)
    ax.vlines(m, 0, L, color=col.thr, ls=dash)
    ax.hlines(L, 0.8, m, color=col.thr, ls=dash)
ax.set_title(rf"$\lambda(\mathbf{{x}})={ratio:.3f}$")
ax.set_xlabel(r"$\mu$")
ax.set_ylabel("likelihood")
ax.legend()

plt.show()
