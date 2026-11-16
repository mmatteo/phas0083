# Example 8.2.7 (Figure 8.4): Likelihood of $\mu$ with $\sigma^2$ at its restricted and unrestricted MLEs, and the resulting likelihood ratio
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([1.1, 0.9, 1.4, 1.0, 1.2])
mu_0 = 1.0


def likelihood(mu, s2):
    # broadcasting: x[:, None] makes x a column, so mu
    # can be an array
    pdf = norm.pdf(x[:, None], mu, np.sqrt(s2))
    return np.prod(pdf, axis=0)


# the MLEs over the whole space, and under H0: mu <= mu_0
mu_hat = x.mean()
s2_hat = np.mean((x - mu_hat)**2)
mu_0_hat = min(mu_0, mu_hat)
s2_0_hat = np.mean((x - mu_0_hat)**2)

# the likelihood ratio
L_0 = likelihood(mu_0_hat, s2_0_hat)[0]
L_hat = likelihood(mu_hat, s2_hat)[0]
print(f"lambda(x) = {L_0 / L_hat:.3f}")

mu = np.linspace(0.8, 1.4, 200)
dark, light = shades(col.like, 2)
fig, ax = plt.subplots()
ax.plot(mu, likelihood(mu, s2_0_hat), color=dark,
        label=r"$\hat\sigma_0^2$")
ax.vlines(mu_0_hat, 0, L_0, color=col.ref, ls=":")
ax.hlines(L_0, mu[0], mu_0_hat, color=col.ref, ls=":")
ax.plot(mu, likelihood(mu, s2_hat), color=light,
        label=r"$\hat\sigma^2$")
ax.vlines(mu_hat, 0, L_hat, color=col.data)
ax.hlines(L_hat, mu[0], mu_hat, color=col.data)
ax.set(xlabel=r"$\mu$", ylabel="likelihood")
ax.legend()

plt.show()
