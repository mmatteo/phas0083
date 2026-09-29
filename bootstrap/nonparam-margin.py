# Nonparametric bootstrap replicates of the sample mean
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([3.54, 5.13, 2.84, 4.48, 1.03, 16.92,
              0.05, 14.05, 2.88, 1.50, 2.71, 1.56])
n = x.size
x_bar = x.mean()
B = 999

# resample the data with replacement
x_star = rng.choice(x, size=(B, n), replace=True)
t_star = x_star.mean(axis=1)

bias_B = t_star.mean() - x_bar
var_B = t_star.var(ddof=1)
print(f"Bias_B*(mean) = {bias_B:.3f}")
print(f"Var_B*(mean)  = {var_B:.3f}")

fig, ax = plt.subplots()
ax.hist(t_star, bins=25, density=True, color=col.hist)
ax.axvline(x_bar, color=col.data, label=r"$\bar{x}$")
ax.set_xlabel("$t^*_i$")
ax.set_ylabel("density")
ax.legend()

plt.show()
