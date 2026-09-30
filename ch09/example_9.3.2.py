# Example 9.3.2 (Figure 9.8): Power functions of the two tests of $H_0:\theta\le1/2$ based on five Bernoulli trials
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

def beta_1(theta):
    """Reject if all five trials succeed."""
    return theta**5


def beta_2(theta):
    """Reject if at least three trials succeed."""
    return (comb(5, 3) * theta**3 * (1 - theta)**2
            + comb(5, 4) * theta**4 * (1 - theta)
            + comb(5, 5) * theta**5)


theta = np.linspace(0, 1, 400)
fig, ax = plt.subplots()
color_1, color_2 = shades(col.cdf, 2)
ax.plot(theta, beta_1(theta), color=color_1,
        label=r"$\beta_1$")
ax.plot(theta, beta_2(theta), color=color_2,
        label=r"$\beta_2$")
ax.axvline(1 / 2, **ref)
ax.set_xlabel(r"$\theta$")
ax.set_ylabel("power")
ax.legend()

plt.show()
