# Example 9.2.7 (Figure 9.4): Likelihood of $\mu$ with $\sigma^2$ at its restricted and unrestricted MLEs, and the resulting likelihood ratio
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([1.1, 0.9, 1.4, 1.0, 1.2])


# the likelihood of (mu, sigma^2): the product of the pdfs
def likelihood(mu, s2):
    L = 1
    for xi in x:
        L = L * norm.pdf(xi, mu, np.sqrt(s2))
    return L


# the MLEs under H0: mu <= 1, and over the whole space
mu_0 = min(1.0, x.mean())
s2_0 = np.mean((x - mu_0)**2)
mu_hat = x.mean()
s2_hat = np.mean((x - mu_hat)**2)

# the likelihood ratio
L_0 = likelihood(mu_0, s2_0)
L_hat = likelihood(mu_hat, s2_hat)
ratio = L_0 / L_hat
print(f"lambda(x) = {ratio:.3f}")

mu = np.linspace(0.8, 1.4, 200)
dark, light = shades(col.like, 2)
fig, ax = plt.subplots()
ax.plot(mu, likelihood(mu, s2_0), color=dark,
        label=r"$\hat\sigma_0^2$")
ax.vlines(mu_0, 0, L_0, color=col.thr, ls=":")
ax.hlines(L_0, 0.8, mu_0, color=col.thr, ls=":")
ax.plot(mu, likelihood(mu, s2_hat), color=light,
        label=r"$\hat\sigma^2$")
ax.vlines(mu_hat, 0, L_hat, color=col.thr, ls="-.")
ax.hlines(L_hat, 0.8, mu_hat, color=col.thr, ls="-.")
ax.set_xlabel(r"$\mu$")
ax.set_ylabel("likelihood")
ax.legend()

plt.show()
