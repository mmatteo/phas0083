# Example 5.2.6 (Figure 5.8): Contours of $f(x,y)\propto e^{-(x^2-xy+y^2)}$ (top); its slices at $y=-1$ and $+1$ divided by their area, the conditional pdfs $f(x\mid y)$, and a slice of the standard bivariate normal (bottom)
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

x = np.linspace(-3, 3, 241)
X, Y = np.meshgrid(x, x)
f = np.exp(-(X**2 - X * Y + Y**2))

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.contour(X, Y, f, levels=6, colors=col.pdf)
ax2.plot(x, norm.pdf(x), color=col.pdf,
         label="standard normal")
for y, color in zip([-1, 1], ["tab:red", "tab:purple"]):
    s = np.exp(-(x**2 - x * y + y**2))
    ax1.axhline(y, color=color, ls="--")
    ax2.plot(x, s / np.trapezoid(s, x), color=color,
             label=rf"$f(x\mid y={y:+d})$")
ax1.set(xlabel="$x$", ylabel="$y$")
ax2.set(xlabel="$x$", ylabel="pdf")
ax2.legend()

plt.show()
