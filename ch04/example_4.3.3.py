# Example 4.3.3 (Figure 4.5): EDF of $N=500$ draws from $\mathcal{N}(0,1)$, with its $0.025$, $0.5$ and $0.975$ quantiles and the true ones
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

N = 500
x = np.sort(rng.normal(0, 1, N))
F_hat = np.arange(1, N + 1) / N

probs = [0.025, 0.5, 0.975]
q_hat = [x[int(np.ceil(N * p)) - 1] for p in probs]
q_true = [norm.ppf(p) for p in probs]
for p, qh, qt in zip(probs, q_hat, q_true):
    print(f"p={p:.3f}: {qh:.3f} (true {qt:.3f})")

fig, ax = plt.subplots()
ax.step(x, F_hat, where="post", color=col.emp,
        label=r"$\hat{F}_N$")
for p, qh in zip(probs, q_hat):
    ax.hlines(p, -4, qh, **thr)
    ax.vlines(qh, 0, p, **thr)
ax.plot(q_true, probs, "x", color=col.data, ms=7, mew=1.5,
        label="true quantile")
ax.set_xlim(-4, 4)
ax.set_xlabel("$x$")
ax.set_ylabel("cdf")
ax.legend()

plt.show()
