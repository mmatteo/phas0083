# Example A.5.2 (Figure A.4): A mixture sample with its signal bin and side bands, and the on/off estimates read from the three counts
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

w, mu, sigma = 0.25, 0, 1       # the mixture
a, b, N = -8, 8, 800            # range, sample size

# the sample, event by event: signal or background, then x
z = rng.random(N) < w
x = np.where(z, rng.normal(mu, sigma, N),
             rng.uniform(a, b, N))
sig_bin, side = (-4, 4), [(-8, -4), (4, 8)]
x_cnt = np.sum((x > -4) & (x < 4))     # the signal bin
y_cnt = N - x_cnt                       # the side bands

# fractions of each component in the bins
w_lam_x = norm.cdf(4) - norm.cdf(-4)   # signal in bin x
w_nu_x, w_nu_y = 0.5, 0.5              # background
nu_hat = y_cnt / w_nu_y
lam_hat = max(0, x_cnt - nu_hat * w_nu_x) / w_lam_x
print(f"generated: {z.sum()} signal, {N - z.sum()} bkg")
print(f"counts: x = {x_cnt}, y = {y_cnt}")
print(f"estimates: lambda {lam_hat:.0f}, nu {nu_hat:.0f}")

fig, ax = plt.subplots()
ax.hist(x, bins=32, range=(a, b), color=col.hist)
for lo, hi in side:
    ax.axvspan(lo, hi, color=col.cdf, alpha=0.15)
ax.axvspan(*sig_bin, color=col.pdf, alpha=0.10)
ax.set_xlabel("$x$")
ax.set_ylabel("counts per bin")

plt.show()
