# Example 4.3.3 (Figure 4.9): ecdf of $N=500$ draws from $\mathcal{N}(0,1)$, with its $0.025$, $0.5$ and $0.975$ quantiles and the true ones
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

N = 500
x = np.sort(rng.normal(0, 1, size=N))

# quantile of the ecdf: the ceil(pN)-th ordered draw
probs = np.array([0.025, 0.5, 0.975])
# pN is rounded first: it is a product of floats
rank = np.ceil(np.round(probs * N, 9))
q_hat = x[rank.astype(int) - 1]
q_true = norm.ppf(probs)
for p, q, q_F in zip(probs, q_hat, q_true):
    print(f"p={p:.3f}: {q:.3f} (true {q_F:.3f})")

x_min = -4
fig, ax = plt.subplots()
ax.ecdf(x, color=col.draws, label=r"$\hat{F}_N$")
ax.hlines(probs, x_min, q_hat, color=col.ref, ls=":")
ax.vlines(q_hat, 0, probs, color=col.ref, ls=":")
ax.plot(q_true, probs, "x", color=col.data, ms=7, mew=1.5,
        label="true quantile")
ax.set(xlim=(x_min, 4), xlabel="$x$", ylabel="cdf")
ax.legend()

plt.show()
