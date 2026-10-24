# Example 5.2.6 (Figure 5.6): Contours of $f(x,y)\propto e^{-(x^2-xy+y^2)}$ (top); its slices at $y=-1$ and $+1$ divided by their area, the conditional pdfs $f(x\mid y)$, and a slice of the standard bivariate normal (bottom)
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.linspace(-3, 3, 241)
X, Y = np.meshgrid(x, x)
f = np.exp(-(X**2 - X * Y + Y**2))

fig, axes = plt.subplots(2, 1)
axes[0].contour(X, Y, f, levels=6, colors=col.ref)
# slices at y = -1 and +1 divided by their area, and the
# slice of the standard bivariate normal, equal at every y
axes[1].plot(x, norm.pdf(x), color=col.ref,
             label="standard normal")
for y, color in zip([-1, 1], shades(col.pdf, 3)):
    s = np.exp(-(x**2 - x * y + y**2))
    axes[0].axhline(y, color=color, ls="--")
    axes[1].plot(x, s / np.trapezoid(s, x), color=color,
                 label=rf"$f(x\mid y={y:+d})$")
axes[0].set_xlabel("$x$")
axes[0].set_ylabel("$y$")
axes[1].set_xlabel("$x$")
axes[1].set_ylabel("pdf")
axes[1].legend()

plt.show()
