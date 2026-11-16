# Example A.6.2 (Figure A.7): Binned likelihood fit of a histogram: the counts, the fitted signal-plus-background expectation and the background alone
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

# draw the numbers of signal and background events
n_s = rng.poisson(400)
n_b = rng.poisson(200)
x = np.concatenate([rng.normal(0, 1, size=n_s),
                    rng.uniform(-4, 4, size=n_b)])
edges = np.linspace(-4, 4, 17)
n, _ = np.histogram(x, bins=edges)

# the templates: the fraction of each component in each bin
s = np.diff(norm.cdf(edges)) / (norm.cdf(4) - norm.cdf(-4))
b = np.diff(edges) / 8


# binned negative log-likelihood, up to constant terms
def nll(p):
    mu = p[0] * s + p[1] * b
    return np.sum(mu - n * np.log(mu))


start = [n.sum() / 2, n.sum() / 2]
result = minimize(nll, start, bounds=[(0, None), (0, None)])
lam_hat, nu_hat = result.x
print(f"generated: {n_s} signal, {n_b} bkg")
print(f"fitted: lambda {lam_hat:.0f}, nu {nu_hat:.0f}")

fig, ax = plt.subplots()
ax.stairs(n, edges, fill=True, color=col.hist, label="data")
ax.stairs(lam_hat * s + nu_hat * b, edges, color=col.pmf,
          label="fit")
ax.stairs(nu_hat * b, edges, color="tab:brown",
          label="background")
ax.set(xlabel="$x$", ylabel="counts per bin")
ax.legend()

plt.show()
