# Example A.6.2 (Figure A.6): Binned likelihood fit of a histogram: the counts, the fitted signal-plus-background expectation and the background alone
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

# Poisson numbers of signal and background events, and the
# sample
n_s = rng.poisson(400)
n_b = rng.poisson(200)
x = np.concatenate([rng.normal(0, 1, n_s),
                    rng.uniform(-4, 4, n_b)])
edges = np.linspace(-4, 4, 17)
n, _ = np.histogram(x, bins=edges)

# the templates: the fraction of each component in each bin
s = np.diff(norm.cdf(edges)) / (norm.cdf(4) - norm.cdf(-4))
b = np.diff(edges) / 8


# the negative log-likelihood of the binned model, up to
# constant terms
def nll(p):
    mu = p[0] * s + p[1] * b
    return np.sum(mu - n * np.log(mu))


start = [n.sum() / 2, n.sum() / 2]
res = minimize(nll, start, bounds=[(0, None), (0, None)])
lam_hat, nu_hat = res.x
print(f"generated: {n_s} signal, {n_b} bkg")
print(f"fitted: lambda {lam_hat:.0f}, nu {nu_hat:.0f}")

fig, ax = plt.subplots()
ax.stairs(n, edges, fill=True, color=col.hist, label="data")
ax.stairs(lam_hat * s + nu_hat * b, edges, color=col.pdf,
          label="fit")
ax.stairs(nu_hat * b, edges, **ref, label="background")
ax.set_xlabel("$x$")
ax.set_ylabel("counts per bin")
ax.legend()

plt.show()
