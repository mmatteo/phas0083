# Example 3.5.3 (Figure 3.13): Poisson pmf for $\nu=0.7,3,10$ (top); binomial pmf with $p=3/N$ approaching the Poisson with $\nu=3$ (bottom)
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.arange(0, 21)
nu_ref = 3

fig, (ax1, ax2) = plt.subplots(2, 1)
for color, nu in zip(shades(col.pmf, 3), [0.7, 3, 10]):
    pmf = poisson.pmf(x, nu)
    modes = x[np.isclose(pmf, pmf.max())]
    print(f"nu={nu}: mode {modes}")
    ax1.plot(x, pmf, "o", color=color, label=rf"$\nu={nu}$")
    ax1.vlines(x, 0, pmf, colors=color)

# binomials with p = nu_ref / N against their Poisson limit
pmf_ref = poisson.pmf(x, nu_ref)
ax2.plot(x, pmf_ref, "o", color=col.ref, fillstyle="none",
         label=rf"Poisson, $\nu={nu_ref}$")
ax2.vlines(x, 0, pmf_ref, colors=col.ref, alpha=0.4)
for color, N in zip(shades(col.pmf, 3), [5, 10, 100]):
    pmf = binom.pmf(x, N, nu_ref / N)
    ax2.plot(x, pmf, "x", color=color, mew=1.5,
             label=f"binomial, $N={N}$")
ax2.set_xlim(-0.5, 10.5)
for ax in (ax1, ax2):
    ax.set_xlabel("number of occurrences")
    ax.set_ylabel("probability")
    ax.legend()

plt.show()
