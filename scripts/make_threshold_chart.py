"""Light and dark PNGs of the "What a threshold costs" chart for the profile README.

Same illustrative lending book as the hero chart on daniel-livingston.streamlit.app: 1,000
applications scored by a calibrated default model whose risk follows Beta(0.5, 3.5) (a 12.5%
default rate). A missed default loses $3,000; turning away a good borrower gives up $1,000. With
calibrated scores the cheapest threshold is C_FP / (C_FP + C_FN) = 0.25, whatever the score
distribution.

Colours are the brand's validated categorical steps (teal, violet, amber), checked with the
dataviz palette validator against GitHub's light (#ffffff) and dark (#0d1117) surfaces. The two
cost components share violet and are told apart by dash and direct label.

    python scripts/make_threshold_chart.py      # writes assets/threshold-cost-{light,dark}.png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

BOOK, COST_FN, COST_FP = 1_000, 3_000, 1_000
RISK_BETA = (0.5, 3.5)
OPTIMUM, USUAL = COST_FP / (COST_FP + COST_FN), 0.5
OUT = Path(__file__).resolve().parent.parent / "assets"

THEMES = {
    "light": dict(surface="#ffffff", ink="#0e1a2b", muted="#3c5a7d", faint="#8a9bb0", grid="#dde4ec",
                  total="#00948c", part="#5b6fd8", optimum="#c2760a"),
    "dark": dict(surface="#0d1117", ink="#f2f5f9", muted="#9fb1c7", faint="#6f86a3", grid="#2b3f58",
                 total="#26a59f", part="#7c80ea", optimum="#c8820f"),
}


def cost_curve():
    """Expected cost of wrong calls at each threshold (decline when risk >= threshold)."""
    a, b = RISK_BETA
    risk = np.linspace(0.0005, 0.9995, 4000)
    share = risk ** (a - 1) * (1 - risk) ** (b - 1)
    share /= share.sum()
    t = np.round(np.arange(0, 1.0001, 0.005), 3)
    approved = np.searchsorted(risk, t)
    defaults = np.concatenate([[0], np.cumsum(risk * share)])
    good = np.concatenate([[0], np.cumsum((1 - risk) * share)])
    missed = BOOK * COST_FN * defaults[approved]
    turned_away = BOOK * COST_FP * (good[-1] - good[approved])
    return t, missed + turned_away, missed, turned_away


def money(x: float) -> str:
    return "$0" if x == 0 else f"${x / 1000:,.0f}k"


def draw(mode: str) -> Path:
    c = THEMES[mode]
    t, total, missed, turned = cost_curve()
    at = lambda x: float(np.interp(x, t, total))  # noqa: E731
    px = 1 / 100  # figure units are pixels at dpi 100; saved at 2x
    plt.rcParams.update({"font.family": "Segoe UI", "font.size": 11})
    fig, ax = plt.subplots(figsize=(900 * px, 400 * px), dpi=100)
    fig.patch.set_facecolor(c["surface"])
    ax.set_facecolor(c["surface"])
    lw = 72 / 100  # points per pixel at dpi 100

    ax.plot(t, turned, color=c["part"], lw=2 * lw, ls=(0, (2, 3)), solid_capstyle="round", label="Good loans turned away")
    ax.plot(t, missed, color=c["part"], lw=2 * lw, ls=(0, (6, 4)), label="Missed defaults")
    ax.plot(t, total, color=c["total"], lw=3 * lw, solid_capstyle="round", label="Total cost", zorder=3)

    # Direct labels where each line runs clear of the others.
    ax.text(0.37, float(np.interp(0.37, t, turned)) + 45_000, "Good loans turned away", color=c["muted"],
            fontsize=10.5, ha="left", va="bottom")
    ax.text(0.80, float(np.interp(0.80, t, missed)) - 60_000, "Missed defaults", color=c["muted"], fontsize=10.5,
            ha="center", va="top")
    ax.text(0.80, at(0.80) + 45_000, "Total cost", color=c["ink"], fontsize=10.5, ha="center", va="bottom",
            fontweight="semibold")

    # The cost-optimal threshold (the one highlight) and the usual 0.50, each with a leader to its label.
    ymax = 900_000
    for x, text, colour, text_colour, label_y in (
        (OPTIMUM, f"Cost-optimal {OPTIMUM:.2f} · {money(at(OPTIMUM))}", c["optimum"], c["ink"], 0.70 * ymax),
        (USUAL, f"Usual {USUAL:.2f} · {money(at(USUAL))}", c["faint"], c["muted"], 0.56 * ymax),
    ):
        ax.plot([x, x], [at(x), label_y - 0.035 * ymax], color=colour, lw=1 * lw, ls=(0, (2, 3)), zorder=4)
        ax.scatter([x], [at(x)], s=(10 * lw) ** 2, color=colour, edgecolors=c["surface"], linewidths=2 * lw, zorder=5)
        ax.text(x - 0.004, label_y, text, color=text_colour, fontsize=10.5, ha="left", va="center",
                fontweight="semibold" if colour == c["optimum"] else "normal", zorder=6)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, ymax)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.2f}"))
    ax.set_yticks([0, 200_000, 400_000, 600_000, 800_000])
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: money(v)))
    ax.set_xlabel("Decision threshold (predicted default risk)", color=c["muted"], fontsize=10.5, labelpad=8)
    ax.grid(axis="y", color=c["grid"], lw=1 * lw)
    ax.set_axisbelow(True)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(c["grid"])
    ax.tick_params(colors=c["muted"], labelsize=10, length=0, pad=6)

    leg = ax.legend(loc="upper right", frameon=False, ncols=3, fontsize=10, handlelength=2.4,
                    bbox_to_anchor=(1.0, 1.12), labelcolor=c["muted"])
    handles = leg.legend_handles
    order = [2, 1, 0]  # total first in the legend
    ax.legend([handles[i] for i in order], [h.get_label() for h in (handles[i] for i in order)],
              loc="upper right", frameon=False, ncols=3, fontsize=10, handlelength=2.4,
              bbox_to_anchor=(1.0, 1.13), labelcolor=c["muted"])

    fig.subplots_adjust(left=0.085, right=0.985, top=0.88, bottom=0.15)
    path = OUT / f"threshold-cost-{mode}.png"
    fig.savefig(path, dpi=200, facecolor=c["surface"])
    plt.close(fig)
    return path


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    t, total, _, _ = cost_curve()
    print("optimum", OPTIMUM, money(float(np.interp(OPTIMUM, t, total))),
          "| usual", USUAL, money(float(np.interp(USUAL, t, total))))
    for m in THEMES:
        print(draw(m))
