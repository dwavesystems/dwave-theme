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

"""Central repository for color palettes and theme constants."""

# Primary Colors
BRAND_MEDIUM_BLUE = "#2A7DE1"
BRAND_MEDIUM_ORANGE = "#F37820"
BRAND_MEDIUM_GREEN = "#17BEBB"
BRAND_DARK_GRAY = "#222222"
BRAND_DARK_BLUE = "#074C91"

# Secondary Colors
BRAND_BRIGHT_BLUE = "#03B8FF"
BRAND_DARK_ORANGE = "#AF4904"
BRAND_DARK_GREEN = "#008C82"
BRAND_LIGHT_PINK = "#FF81E1"
BRAND_MEDIUM_PINK = "#E83E8C"
BRAND_BRIGHT_GRAY = "#F0F0F0"

# Light Mode Neutrals
LIGHT_BG_CANVAS = "#FFFFFF"
LIGHT_BG_PLOT = "#FFFFFF"
LIGHT_TEXT_PRIMARY = "#333333"
LIGHT_TEXT_SECONDARY = "#666666"
LIGHT_GRID = "#E5E5E5"
LIGHT_AXIS_SPINE = "#CCCCCC"

# Dark Mode Neutrals
DARK_BG_CANVAS = "#121212"
DARK_BG_PLOT = "#121212"
DARK_TEXT_PRIMARY = "#E0E0E0"
DARK_TEXT_SECONDARY = "#A0A0A0"
DARK_GRID = "#333333"
DARK_AXIS_SPINE = "#444444"

PALETTES: dict[str, dict[str, list[str]]] = {
    "qualitative": {
        "light": [
            BRAND_MEDIUM_BLUE,
            BRAND_MEDIUM_ORANGE,
            BRAND_MEDIUM_GREEN,
            BRAND_DARK_GRAY,
            BRAND_DARK_BLUE,
            BRAND_BRIGHT_BLUE,
            BRAND_MEDIUM_PINK,
            BRAND_DARK_ORANGE,
            BRAND_LIGHT_PINK,
            BRAND_DARK_GREEN,
        ],
        "dark": [
            BRAND_MEDIUM_BLUE,
            BRAND_MEDIUM_ORANGE,
            BRAND_MEDIUM_GREEN,
            BRAND_BRIGHT_GRAY,
            BRAND_DARK_BLUE,
            BRAND_BRIGHT_BLUE,
            BRAND_MEDIUM_PINK,
            BRAND_DARK_ORANGE,
            BRAND_LIGHT_PINK,
            BRAND_DARK_GREEN,
        ],
    },
    "sequential": {
        "light": [
            "#2595F5",
            "#51A6F7",
            "#70B6F9",
            "#8FC6FB",
            "#ADD5FC",
            "#CCE5FD",
            "#EBF5FF",
        ],
        "dark": [
            "#0858A7",
            "#0B5093",
            "#0E487F",
            "#123F6B",
            "#153757",
            "#192E44",
            "#1C2630",
        ],
    },
}

THEMES: dict[str, dict[str, str]] = {
    "light": {
        "bg_canvas": LIGHT_BG_CANVAS,
        "bg_plot": LIGHT_BG_PLOT,
        "text_primary": LIGHT_TEXT_PRIMARY,
        "text_secondary": LIGHT_TEXT_SECONDARY,
        "axis_label": LIGHT_TEXT_SECONDARY,
        "grid": LIGHT_GRID,
        "axis_line": LIGHT_AXIS_SPINE,
    },
    "dark": {
        "bg_canvas": DARK_BG_CANVAS,
        "bg_plot": DARK_BG_PLOT,
        "text_primary": DARK_TEXT_PRIMARY,
        "text_secondary": DARK_TEXT_SECONDARY,
        "axis_label": DARK_TEXT_PRIMARY,
        "grid": DARK_GRID,
        "axis_line": DARK_AXIS_SPINE,
    },
}


def get_palettes(category: str | None = None) -> list[tuple[str, list[str]]]:
    """Returns ``(label, colors)`` pairs for all palettes or a specific category.

    Args:
        category: The specific palette category to retrieve (e.g., ``'qualitative'``).
            If ``None``, retrieves all available categories.

    Returns:
        list[tuple[str, list[str]]]: ``("<category> : <variant>", colors)`` pairs.

    Raises:
        ValueError: If ``category`` does not exist in ``PALETTES`` or no palettes are found.
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

    palettes: list[tuple[str, list[str]]] = []
    for cat in target_cats:
        for variant_name, colors in PALETTES[cat].items():
            palettes.append((f"{cat} : {variant_name}", colors))

    if not palettes:
        raise ValueError("No palettes found to display.")

    return palettes
