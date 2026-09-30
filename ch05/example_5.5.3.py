# Example 5.5.3 (Figure 5.16): Simulated $P=VI$ with small (top) and large (bottom) relative uncertainties, and normal pdfs with the exact and delta-method variances
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

rng = np.random.default_rng(1)
N = 2_000_000
cases = [(12, 0.5, 2, 0.1, "small uncertainties"),
         (12, 3, 2, 0.5, "large uncertainties")]

fig, axes = plt.subplots(2, 1)
for ax, (mu_V, sd_V, mu_I, sd_I, title) in zip(axes, cases):
    var_delta = mu_V**2 * sd_I**2 + mu_I**2 * sd_V**2
    missing = sd_V**2 * sd_I**2
    var_exact = var_delta + missing

    V = rng.normal(mu_V, sd_V, N)
    I = rng.normal(mu_I, sd_I, N)  # noqa: E741
    P = V * I
    bias = 100 * missing / var_exact
    print(f"{title}:")
    print(f"  exact {var_exact:.4f}, delta {var_delta:.4f}")
    var_sim = P.var(ddof=1)
    print(f"  missing {missing:.4f}, sim {var_sim:.4f}")
    print(f"  bias {bias:.2f}%")

    u = np.linspace(P.min(), P.max(), 200)
    ax.hist(P, bins=30, density=True, color=col.hist,
            label="simulation")
    ax.plot(u, norm.pdf(u, mu_V * mu_I, var_exact**0.5),
            **ref, label="exact")
    ax.plot(u, norm.pdf(u, mu_V * mu_I, var_delta**0.5),
            color=col.ref, ls="-.", label="delta")
    ax.set_title(title)
    ax.set_xlabel("$P$")
    ax.set_ylabel("density")
axes[0].legend()

plt.show()
