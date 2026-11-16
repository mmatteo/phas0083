# Example 4.3.2 (Figure 4.8): ecdf of $N$ draws from $\mathcal{N}(0,1)$ and the true cdf, for $N=20$, $200$, $2000$ (top to bottom)
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

u = np.linspace(-4, 4, 400)

fig, axes = plt.subplots(3, 1, sharex=True)
for ax, N in zip(axes, [20, 200, 2000]):
    # the ecdf: a step of 1/N at each ordered draw
    x = np.sort(rng.normal(0, 1, size=N))
    F_hat = np.arange(1, N + 1) / N
    ax.plot(u, norm.cdf(u), color=col.cdf, label="$F$")
    ax.step(x, F_hat, where="post", color=col.draws,
            label=r"$\hat{F}_N$")
    ax.set(title=f"$N={N}$", ylabel="cdf")
axes[-1].set(xlim=(-4, 4), xlabel="$x$")
axes[0].legend()

plt.show()
