# Example 8.5.2 (Figure 8.10): Power of the level-0.05 one-sided test on the mean of a normal sample as a function of $\theta$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

n = 5
theta_0 = 1.0
alpha = 0.05
m = 20_000
theta_values = np.linspace(0, 2.5, 26)
c = 2.71  # the threshold of the previous example


def nlrt(x_bar):
    return n * np.maximum(0, x_bar - theta_0)**2


# power at each theta: the fraction of samples rejected
power = []
for theta in theta_values:
    x = rng.normal(theta, 1, size=(m, n))
    x_bar = x.mean(axis=1)
    power.append(np.mean(nlrt(x_bar) > c))
for i in [10, 20]:
    print(f"power at theta = {theta_values[i]:.1f}: "
          f"{power[i]:.3f}")

fig, ax = plt.subplots()
ax.plot(theta_values, power, "o-", color=col.draws)
ax.axhline(alpha, color=col.ref, ls=":")
ax.set(xlabel=r"$\theta$", ylabel="power")

plt.show()
