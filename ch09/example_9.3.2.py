# Example 9.3.2 (Figure 9.13): The count with a known background: the test statistic of the observed count (black) and the confidence belt (blue), below the thresholds found at each tested value (dotted); the $95\%$ confidence interval is marked on the axis
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x_obs = 65
nu = 50
alpha = 0.05
m = 99_999
lambda_values = np.linspace(0, 40, 81)


def nlrt(x, lambda_0):
    lambda_hat = np.maximum(0, x - nu)
    return (-2 * poisson.logpmf(x, lambda_0 + nu)
            + 2 * poisson.logpmf(x, lambda_hat + nu))


# find the threshold at each lambda_0
k = round((m + 1) * (1 - alpha)) - 1
threshold = np.zeros_like(lambda_values)
for i, lambda_0 in enumerate(lambda_values):
    x_sim = rng.poisson(lambda_0 + nu, size=m)
    T_sorted = np.sort(nlrt(x_sim, lambda_0))
    threshold[i] = T_sorted[k]

# interval: the values of lambda_0 the test accepts
t_obs = nlrt(x_obs, lambda_values)
accepted = lambda_values[t_obs <= threshold]
print(f"estimate: {max(0, x_obs - nu)}")
print(f"interval: [{accepted[0]}, {accepted[-1]}]")

fig, ax = plt.subplots()
ax.fill_between(lambda_values, 0, threshold, color=col.pdf,
                alpha=0.15)
ax.plot(lambda_values, threshold, color=col.draws, ls=":")
ax.plot(lambda_values, t_obs, color=col.data)
ax.plot(accepted[[0, -1]], [0, 0], color="tab:red", lw=3,
        clip_on=False)
ax.set(ylim=(0, 8), xlabel=r"$\lambda_0$",
       ylabel=r"$-2\log\lambda$")

plt.show()
