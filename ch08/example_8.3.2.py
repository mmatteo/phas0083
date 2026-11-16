# Example 8.3.2 (Figure 8.6): Power functions of the two tests of $H_0:\theta\le1/2$ based on five Bernoulli trials
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

# the first rule rejects if all five trials succeed
def beta_1(theta):
    return theta**5


# the second rule rejects if at least three succeed
def beta_2(theta):
    return (comb(5, 3) * theta**3 * (1 - theta)**2
            + comb(5, 4) * theta**4 * (1 - theta)
            + comb(5, 5) * theta**5)


theta = np.linspace(0, 1, 400)
dark, light = shades(col.cdf, 2)
fig, ax = plt.subplots()
ax.plot(theta, beta_1(theta), color=dark,
        label=r"$\beta_1$")
ax.plot(theta, beta_2(theta), color=light,
        label=r"$\beta_2$")
ax.axvline(1 / 2, color=col.ref, ls="--")
ax.set(xlabel=r"$\theta$", ylabel="power")
ax.legend()

plt.show()
