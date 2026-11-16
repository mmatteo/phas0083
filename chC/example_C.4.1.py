# Example C.4.1 (Figure C.2): Confidence regions for the offset and the gain from the chi-square contours, and the estimates of 1000 simulated calibrations
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

E = np.array([60, 122, 356, 662, 1173, 1332])
sigma = np.array([5, 5, 8, 10, 15, 15])
# sums of the normal equations without the heights
wt = 1 / sigma**2
S = wt.sum()
Sx = (wt * E).sum()
Sxx = (wt * E**2).sum()
D = S * Sxx - Sx**2


# the least-squares offset and gain of each row of h
def fit(h):
    Sy = (wt * h).sum(axis=-1)
    Sxy = (wt * E * h).sum(axis=-1)
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
c68, c95 = chi2.ppf([0.68, 0.95], df=2)

# simulate calibrations: fraction inside the 68% region
m = 1000
h_sim = rng.normal(a_hat + b_hat * E, sigma,
                   size=(m, E.size))
a_sim, b_sim = fit(h_sim)
da = a_sim - a_hat
db = b_sim - b_hat
inside = np.mean(S * da**2 + Sxx * db**2
                 + 2 * Sx * da * db < c68)
print(f"fits inside the 68% region: {inside:.2f}")

fig, ax = plt.subplots()
ax.plot(a_sim, b_sim, "o", color=col.draws, ms=2,
        alpha=0.3)
contour = ax.contour(a, b, dchi2, levels=[c68, c95],
                     colors=col.like)
ax.clabel(contour, fmt={c68: "68%", c95: "95%"})
ax.plot(a_hat, b_hat, "*", color=col.data, ms=8)
ax.set_xlabel("offset $a$ [channels]")
ax.set_ylabel("gain $b$ [channels/keV]")

plt.show()
