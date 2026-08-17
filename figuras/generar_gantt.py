#!/usr/bin/env python3
"""Genera diagramas Gantt (1 fila CPU) para los sistemas planificables."""

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

matplotlib.use("Agg")

OUT = Path(__file__).resolve().parent

COLORS = {
    "T1": "#2563eb",
    "T2": "#ea580c",
    "T3": "#16a34a",
    "T4": "#9333ea",
    "idle": "#d1d5db",
}

# segmentos: (desde, hasta, tarea)
SYSTEMS = [
    {
        "id": 2,
        "title": "Sistema 2 — primeros 24 u.t. (T_M = 90)",
        "tmax": 24,
        "segments": [
            (0, 1, "T1"),
            (1, 3, "T2"),
            (3, 5, "T3"),
            (5, 6, "idle"),
            (6, 7, "T1"),
            (7, 10, "idle"),
            (10, 12, "T2"),
            (12, 13, "T1"),
            (13, 18, "idle"),
            (18, 19, "T1"),
            (19, 20, "T3"),
            (20, 22, "T2"),
            (22, 23, "T3"),
            (23, 24, "idle"),
        ],
    },
    {
        "id": 3,
        "title": "Sistema 3 — primeras 33 u.t. (T_M = 1320)",
        "tmax": 33,
        "segments": [
            (0, 1, "T1"),
            (1, 4, "T2"),
            (4, 8, "T3"),
            (8, 9, "T1"),
            (9, 15, "T4"),
            (15, 16, "T2"),
            (16, 17, "T1"),
            (17, 19, "T2"),
            (19, 20, "idle"),
            (20, 24, "T3"),
            (24, 25, "T1"),
            (25, 31, "T4"),
            (31, 32, "T2"),
            (32, 33, "T1"),
        ],
    },
]


def draw_gantt(system: dict) -> Path:
    tmax = system["tmax"]
    fig_w = max(10, tmax * 0.45)
    fig, ax = plt.subplots(figsize=(fig_w, 2.2), dpi=150)
    y, h = 0.35, 0.5

    for start, end, task in system["segments"]:
        dur = end - start
        ax.barh(
            y,
            dur,
            left=start,
            height=h,
            color=COLORS[task],
            edgecolor="white",
            linewidth=1.2,
            align="center",
        )
        if dur >= 0.8:
            ax.text(
                start + dur / 2,
                y,
                task,
                ha="center",
                va="center",
                fontsize=9 if dur >= 1.5 else 8,
                fontweight="bold",
                color="white" if task != "idle" else "#4b5563",
            )

    ax.set_xticks(range(int(tmax) + 1))
    ax.set_xticklabels(range(int(tmax) + 1), fontsize=9)
    ax.set_xlim(0, tmax)
    ax.set_ylim(0, 1)
    ax.set_yticks([y])
    ax.set_yticklabels(["CPU"], fontsize=11, fontweight="bold")
    ax.grid(axis="x", linestyle="--", alpha=0.35)
    ax.set_xlabel("Tiempo (u.t.)", fontsize=10)
    ax.set_title(system["title"], fontsize=12, fontweight="bold", pad=12)

    used = sorted({task for _, _, task in system["segments"]})
    patches = [mpatches.Patch(color=COLORS[task], label=task) for task in used]
    ax.legend(
        handles=patches,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.22),
        ncol=len(patches),
        frameon=False,
        fontsize=9,
    )

    fig.tight_layout()
    out = OUT / f"gantt-sistema-{system['id']}.png"
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return out


def main() -> None:
    for system in SYSTEMS:
        path = draw_gantt(system)
        print("saved", path)


if __name__ == "__main__":
    main()
