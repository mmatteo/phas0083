# Example 3.5.3 (Figure 3.12): Poisson pmf for $\nu=0.7,3,10$ (top); binomial pmf with $p=3/N$ approaching the Poisson with $\nu=3$ (bottom)
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

def poisson_modes(nu):
    """Modes of a Poisson: two if nu is an integer."""
    if abs(nu - round(nu)) < 1e-12:
        return int(nu - 1), int(nu)
    return (int(np.floor(nu)),)


x = np.arange(0, 21)
nu_values = [0.7, 3, 10]
nu_ref = 3                # mean of the binomial comparison
N_values = [5, 10, 100]   # p = nu_ref / N

fig, axes = plt.subplots(2, 1)
for color, nu in zip(shades(col.pdf, 3), nu_values):
    pmf = poisson.pmf(x, nu)
    axes[0].vlines(x, 0, pmf, colors=[color])
    axes[0].plot(x, pmf, "o", color=color,
                 label=rf"$\nu={nu}$")

# the Poisson is the limit the binomials approach
pmf_ref = poisson.pmf(x, nu_ref)
axes[1].vlines(x, 0, pmf_ref, colors=col.ref, alpha=0.4)
axes[1].plot(x, pmf_ref, "o", color=col.ref,
             fillstyle="none",
             label=rf"Poisson, $\nu={nu_ref}$")
for color, N in zip(shades(col.pdf, 3), N_values):
    pmf = binom.pmf(x, N, nu_ref / N)
    axes[1].plot(x, pmf, "x", color=color, mew=1.5,
                 label=f"binomial, $N={N}$")
axes[1].set_xlim(-0.5, 10.5)
for ax in axes:
    ax.set_ylabel("probability")
    ax.set_xlabel("number of occurrences")
    ax.legend()

print("Poisson modes:")
for nu in nu_values:
    print(f"  nu={nu}: {poisson_modes(nu)}")
print(f"Binomial modes, mean {nu_ref}:")
for N in N_values:
    mode = x[np.argmax(binom.pmf(x, N, nu_ref / N))]
    print(f"  N={N}: {mode}")

plt.show()
