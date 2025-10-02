"""
Provides a function to apply the customizable theme for Matplotlib plots.
"""

from pathlib import Path
from typing import Literal
import matplotlib.pyplot as plt
from cycler import cycler

from ._colors import COLOR_PALETTES


def apply_theme_matplotlib(
    mode: Literal["light", "dark"] = "light",
    palette: str = "qualitative",
    transparent: bool = False,
) -> None:
    """
    Applies the custom theme to Matplotlib.

    Args:
        mode: The theme mode, either 'light' or 'dark'.
        palette: The name of the color palette to use.
        transparent: If True, sets figure background to be transparent.

    Examples:
        >>> import matplotlib.pyplot as plt
        >>> apply_theme_matplotlib(mode='dark')
        >>> fig, ax = plt.subplots()
        >>> ax.plot([1, 2, 3])
        [<matplotlib.lines.Line2D object at ...>]
        >>> plt.close(fig)
    """
    if palette not in COLOR_PALETTES:
        raise ValueError(
            f"Palette '{palette}' not found. Available: {list(COLOR_PALETTES.keys())}"
        )

    base_style_path = Path(__file__).parent / "theme.mplstyle"
    plt.style.use(str(base_style_path))

    if mode == "dark":
        colorway = COLOR_PALETTES.get("qualitative_dark", COLOR_PALETTES[palette])
        font_color = "white"
        bg_color = "#121212"
    else:
        colorway = COLOR_PALETTES[palette]
        font_color = "#333333"
        bg_color = "white"

    plt.rcParams.update(
        {
            "figure.facecolor": bg_color,
            "axes.facecolor": bg_color,
            "text.color": font_color,
            "axes.labelcolor": font_color,
            "axes.titlecolor": font_color,
            "xtick.color": font_color,
            "ytick.color": font_color,
            "axes.edgecolor": font_color,
        }
    )

    color_cycle = [f"#{c.lstrip('#')}" for c in colorway]
    plt.rcParams["axes.prop_cycle"] = cycler(color=color_cycle)

    plt.rcParams["savefig.transparent"] = transparent
    if transparent:
        plt.rcParams["figure.facecolor"] = "none"
        plt.rcParams["axes.facecolor"] = "none"
