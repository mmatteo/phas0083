# Example 12.2.2 (Figure 12.4): Probability of more than $x$ counts under $H_0:\nu=2000$, and the observed count
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

nu = 2000
x_obs = 2100
x = np.arange(1900, 2200)

# p-value: the survival function at the observed count
p_value = poisson.sf(x_obs, nu)
print(f"p-value of x_obs={x_obs}: {p_value:.3f}")

sf = poisson.sf(x, nu)
fig, ax = plt.subplots()
ax.plot(x, sf, color=col.cdf, label="$1-F(x)$ under $H_0$")
ax.axvline(x_obs, color=col.data,
           label=r"$x_\mathrm{obs}$")
ax.set(xlabel="$x$ (number of counts)", ylabel="$1-F(x)$")
ax.legend()

plt.show()
