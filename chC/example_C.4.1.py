# Example C.4.1 (Figure C.2): Confidence regions for the offset and the gain from the chi-square contours, and the estimates of 1000 simulated calibrations
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

E = np.array([60, 122, 356, 662, 1173, 1332])
sigma = np.array([5, 5, 8, 10, 15, 15])
wt = 1 / sigma**2
S, Sx, Sxx = wt.sum(), (wt * E).sum(), (wt * E**2).sum()
D = S * Sxx - Sx**2


def fit(h):
    """Least-squares offset and gain of the heights h."""
    Sy, Sxy = (wt * h).sum(), (wt * E * h).sum()
    return ((Sxx * Sy - Sx * Sxy) / D,
            (S * Sxy - Sx * Sy) / D)


a_hat, b_hat = fit(rng.normal(20 + 1.5 * E, sigma))

# the chi-square above its minimum is exactly quadratic
a, b = np.meshgrid(np.linspace(a_hat - 15, a_hat + 15, 200),
                   np.linspace(b_hat - .03, b_hat + .03,
                               200))
dchi2 = (S * (a - a_hat)**2 + Sxx * (b - b_hat)**2
         + 2 * Sx * (a - a_hat) * (b - b_hat))

# 1000 simulated calibrations from the fitted line
h_star = rng.normal(a_hat + b_hat * E, sigma, (1000, 6))
stars = np.array([fit(h) for h in h_star])
da, db = stars[:, 0] - a_hat, stars[:, 1] - b_hat
inside = np.mean(S * da**2 + Sxx * db**2
                 + 2 * Sx * da * db < 2.30)
print(f"simulated fits inside the 68% region: {inside:.2f}")

fig, ax = plt.subplots()
ax.plot(stars[:, 0], stars[:, 1], "o", color=col.emp, ms=1,
        alpha=0.3)
cs = ax.contour(a, b, dchi2, levels=[2.30, 5.99],
                colors=col.like)
ax.clabel(cs, fmt={2.30: "68%", 5.99: "95%"})
ax.plot(a_hat, b_hat, "*", color=col.data, ms=8)
ax.set_xlabel("offset $a$ [channels]")
ax.set_ylabel("gain $b$ [channels/keV]")

plt.show()
