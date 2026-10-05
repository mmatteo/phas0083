# Example 4.1.1 (Figure 4.3): Draws from $f(x)=2x$ by inverse-transform (top) and rejection (bottom) sampling, with the pdf
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

N = 20000

# inverse transform: F(x) = x^2, so x = sqrt(u)
u = rng.uniform(0, 1, N)
x_inv = np.sqrt(u)

# rejection: envelope uniform on [0, 1] x [0, 2]
x_env = rng.uniform(0, 1, 3 * N)
v_env = rng.uniform(0, 2, 3 * N)
accepted = x_env[v_env <= 2 * x_env]
efficiency = accepted.size / (3 * N)
x_rej = accepted[:N]
print(f"rejection efficiency: {efficiency:.2f}"
      " (expected 0.50)")

t = np.linspace(0, 1, 200)
fig, axes = plt.subplots(2, 1, sharex=True)
for ax, x, title in zip(axes, [x_inv, x_rej],
                        ["inverse transform", "rejection"]):
    ax.hist(x, bins=20, density=True, color=col.hist)
    ax.plot(t, 2 * t, **ref)
    ax.set_title(title)
    ax.set_ylabel("density")
axes[-1].set_xlabel("$x$")

plt.show()
