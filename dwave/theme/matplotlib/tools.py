# Copyright 2025 D-Wave
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.axes import Axes

from dwave.theme.core.colors import PALETTES


def _plot_swatches(ax: Axes, colors: list[str], title: str) -> None:
    """Internal helper to draw a simple row of color swatches on an axis."""
    rgb_values = [mcolors.to_rgb(c) for c in colors]

    ax.imshow([rgb_values], aspect="auto")

    ax.set_yticks([])
    ax.set_xticks(range(len(colors)))
    ax.set_xticklabels(colors, rotation=90, fontsize=8)
    ax.set_title(title, loc="left", fontsize=10, fontweight="bold")

    for spine in ax.spines.values():
        spine.set_visible(False)


def show_palettes(category: str | None = None) -> None:
    """Plots the available color palettes defined in the core theme.

    This creates a figure displaying the hex codes and colors for visualizing.

    Args:
        category: The specific palette category to show (e.g., 'qualitative').
            If ``None``, shows all available categories.

    Raises:
        ValueError: If the provided category does not exist in the core definitions.
        ValueError: If no palettes are found to display.

    Examples:
        >>> # Show everything
        >>> from dwave.theme.matplotlib import show_palettes
        >>> show_palettes()

        >>> # Show only qualitative palettes
        >>> show_palettes("qualitative")
    """
    if category:
        if category not in PALETTES:
            raise ValueError(
                f"Palette category '{category}' not found. "
                f"Available: {sorted(PALETTES.keys())}"
            )
        target_cats = [category]
    else:
        target_cats = sorted(PALETTES.keys())

    plot_list = []
    for cat in target_cats:
        variants = PALETTES[cat]
        for variant_name, colors in variants.items():
            full_name = f"{cat} : {variant_name}"
            plot_list.append((full_name, colors))

    if not plot_list:
        raise ValueError("No palettes found to display.")

    n_plots = len(plot_list)
    _, axes = plt.subplots(n_plots, 1, figsize=(8, 1.5 * n_plots), dpi=150)

    if n_plots == 1:
        axes = [axes]

    for ax, (title, colors) in zip(axes, plot_list):
        _plot_swatches(ax, colors, title)

    plt.tight_layout()
    plt.show()
