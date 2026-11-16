# Example 11.5.2 (Figure 11.6): Bootstrap replicates of the sample median under the fitted exponential model, with the observed median $t$ and the half-life of the fitted model
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([3.54, 5.13, 2.84, 4.48, 1.03, 16.92,
              0.05, 14.05, 2.88, 1.50, 2.71, 1.56])
n = x.size
x_bar = x.mean()
B = 999

# estimate on the data, and parameter of the fitted model
t = np.median(x)
half_life = x_bar * np.log(2)

# draw B bootstrap samples and compute their medians
x_star = rng.exponential(scale=x_bar, size=(B, n))
t_star = np.median(x_star, axis=1)

# bias and variance, with the simulation error of the bias
bias_B = t_star.mean() - half_life
var_B = t_star.var(ddof=1)
sim_error = np.sqrt(var_B / B)
print(f"Bias_B*(median) = {bias_B:.2f} +- {sim_error:.2f}")
print(f"Var_B*(median)  = {var_B:.2f}")

label = r"$\bar{x}\log 2$"
fig, ax = plt.subplots()
ax.hist(t_star, bins=25, density=True, color=col.hist)
ax.axvline(t, color=col.data, label="$t$")
ax.axvline(half_life, color=col.ref, ls="--", label=label)
ax.set(xlabel="$t^*_i$", ylabel="density")
ax.legend()

plt.show()
