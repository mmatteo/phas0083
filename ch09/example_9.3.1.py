# Example 9.3.1 (Figure 9.12): The decay times: the test statistic of the observed sample (black) and the confidence belt (blue), below the thresholds found at each tested value (dotted); the $90\%$ confidence interval is marked on the axis
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([3.54, 5.13, 2.84, 4.48, 1.03, 16.92,
              0.05, 14.05, 2.88, 1.50, 2.71, 1.56])
n = x.size
alpha = 0.10
m = 9_999
lambda_values = np.linspace(2, 12, 201)


def nlrt(x_bar, lambda_0):
    r = x_bar / lambda_0
    return 2 * n * (r - 1 - np.log(r))


# find the threshold at each lambda_0
k = round((m + 1) * (1 - alpha)) - 1
threshold = np.zeros_like(lambda_values)
for i, lambda_0 in enumerate(lambda_values):
    x_sim = rng.exponential(scale=lambda_0, size=(m, n))
    T_sorted = np.sort(nlrt(x_sim.mean(axis=1), lambda_0))
    threshold[i] = T_sorted[k]

# interval: the values of lambda_0 the test accepts
t_obs = nlrt(x.mean(), lambda_values)
accepted = lambda_values[t_obs <= threshold]
print(f"estimate: {x.mean():.2f}")
print(f"interval: [{accepted[0]:.2f}, {accepted[-1]:.2f}]")

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
