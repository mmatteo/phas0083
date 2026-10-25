# Example C.4.1 (Figure C.2): Confidence regions for the offset and the gain from the chi-square contours, and the estimates of 1000 simulated calibrations
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

E = np.array([60, 122, 356, 662, 1173, 1332])
sigma = np.array([5, 5, 8, 10, 15, 15])
# the sums of the normal equations that do not depend on
# the measured heights
wt = 1 / sigma**2
S = wt.sum()
Sx = (wt * E).sum()
Sxx = (wt * E**2).sum()
D = S * Sxx - Sx**2


# the least-squares offset and gain of the heights h
def fit(h):
    Sy = (wt * h).sum()
    Sxy = (wt * E * h).sum()
    a_hat = (Sxx * Sy - Sx * Sxy) / D
    b_hat = (S * Sxy - Sx * Sy) / D
    return a_hat, b_hat


a_hat, b_hat = fit(rng.normal(20 + 1.5 * E, sigma))

# the chi-square above its minimum is exactly quadratic
a, b = np.meshgrid(np.linspace(a_hat - 15, a_hat + 15, 200),
                   np.linspace(b_hat - .03, b_hat + .03,
                               200))
dchi2 = (S * (a - a_hat)**2 + Sxx * (b - b_hat)**2
         + 2 * Sx * (a - a_hat) * (b - b_hat))

# 1000 simulated calibrations from the fitted line, and
# the fraction of their estimates inside the 68% region
B = 1000
stars = np.zeros((B, 2))
for i in range(B):
    h_star = rng.normal(a_hat + b_hat * E, sigma)
    stars[i] = fit(h_star)
da = stars[:, 0] - a_hat
db = stars[:, 1] - b_hat
inside = np.mean(S * da**2 + Sxx * db**2
                 + 2 * Sx * da * db < 2.30)
print(f"fits inside the 68% region: {inside:.2f}")

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
