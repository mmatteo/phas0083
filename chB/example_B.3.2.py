# Example B.3.2 (Figure B.6): Negative log-likelihood of the mixture weight $w$ for a sample of seven values (top), and the fitted mixture with its components over the sample (bottom)
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.array([1.1, 0.9, 1.4, 1.0, 1.2, 0.4, 1.8])
mu, sigma = 1.2, 0.2        # the peak, known
a, b = 0, 2                 # the measured range


def f_s(x):
    return norm.pdf(x, mu, sigma)


def f_b(x):
    return np.full(np.shape(x), 1 / (b - a))


def nll(w):
    """Negative log-likelihood of the mixture weight."""
    return -np.sum(np.log(w * f_s(x) + (1 - w) * f_b(x)))


res = minimize_scalar(nll, bounds=(0, 1), method="bounded")
w_hat = res.x
print(f"MLE of the weight: {w_hat:.2f}")

w = np.linspace(0.01, 0.99, 200)
t = np.linspace(a, b, 200)
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(w, [nll(wi) for wi in w], color=col.like)
ax1.axvline(w_hat, **thr, label=rf"$\hat w={w_hat:.2f}$")
ax1.set_xlabel("$w$")
ax1.set_ylabel("negative log-likelihood")
ax1.legend()
ax2.vlines(x, 0, 0.5, color=col.data, label="sample")
ax2.plot(t, w_hat * f_s(t) + (1 - w_hat) * f_b(t),
         color=col.pdf, label="mixture")
ax2.plot(t, w_hat * f_s(t), **ref, label="signal")
ax2.plot(t, (1 - w_hat) * f_b(t), **thr, label="background")
ax2.set_xlabel("$x$")
ax2.set_ylabel("pdf")
ax2.legend()

plt.show()
