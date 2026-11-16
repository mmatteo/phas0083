# Example B.3.2 (Figure B.6): Negative log-likelihood of the mixture weight $w$ for a sample of seven values (top), and the fitted mixture with its components over the sample (bottom)
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([1.1, 0.9, 1.4, 1.0, 1.2, 0.4, 1.8])
# the peak, known
mu = 1.2
sigma = 0.2
# the measured range
a = 0
b = 2


# signal and flat background pdfs
def f_s(x):
    return norm.pdf(x, mu, sigma)


def f_b(x):
    return np.full(np.shape(x), 1 / (b - a))


def nll(w):
    return -np.sum(np.log(w * f_s(x) + (1 - w) * f_b(x)))


result = minimize_scalar(nll, bounds=(0, 1))
w_hat = result.x
print(f"MLE of the weight: {w_hat:.2f}")

# the negative log-likelihood over a grid of weights
w_grid = np.linspace(0.01, 0.99, 200)
nll_grid = np.array([nll(w) for w in w_grid])

u = np.linspace(a, b, 200)
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(w_grid, nll_grid, color=col.like)
ax1.axvline(w_hat, color=col.data,
            label=rf"$\hat w={w_hat:.2f}$")
ax1.set(xlabel="$w$", ylabel="negative log-likelihood")
ax1.legend()
ax2.plot(x, np.zeros_like(x), "|", color=col.data, ms=8,
         label="sample")
ax2.plot(u, w_hat * f_s(u) + (1 - w_hat) * f_b(u),
         color=col.pdf, label="mixture")
ax2.plot(u, w_hat * f_s(u), color="tab:red",
         label=r"$\hat w\,f_s$")
ax2.plot(u, (1 - w_hat) * f_b(u), color="tab:brown",
         label=r"$(1-\hat w)\,f_b$")
ax2.set(xlabel="$x$", ylabel="weighted pdf")
ax2.legend()

plt.show()
