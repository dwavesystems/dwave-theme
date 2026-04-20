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
_BRAND_MEDIUM_BLUE = "#2A7DE1"
_BRAND_MEDIUM_ORANGE = "#F37820"
_BRAND_MEDIUM_GREEN = "#17BEBB"
_BRAND_DARK_GRAY = "#222222"
_BRAND_DARK_BLUE = "#074C91"

# Secondary Colors
_BRAND_BRIGHT_BLUE = "#03B8FF"
_BRAND_DARK_ORANGE = "#AF4904"
_BRAND_DARK_GREEN = "#008C82"
_BRAND_LIGHT_PINK = "#FF81E1"
_BRAND_MEDIUM_PINK = "#E83E8C"
_BRAND_BRIGHT_GRAY = "#F0F0F0"

# Light Mode Neutrals
_LIGHT_BG_CANVAS = "#FFFFFF"
_LIGHT_BG_PLOT = "#FFFFFF"
_LIGHT_TEXT_PRIMARY = "#333333"
_LIGHT_TEXT_SECONDARY = "#666666"
_LIGHT_GRID = "#E5E5E5"
_LIGHT_AXIS_SPINE = "#CCCCCC"

# Dark Mode Neutrals
_DARK_BG_CANVAS = "#121212"
_DARK_BG_PLOT = "#121212"
_DARK_TEXT_PRIMARY = "#E0E0E0"
_DARK_TEXT_SECONDARY = "#A0A0A0"
_DARK_GRID = "#333333"
_DARK_AXIS_SPINE = "#444444"

PALETTES: dict[str, dict[str, list[str]]] = {
    "qualitative": {
        "light": [
            _BRAND_MEDIUM_BLUE,
            _BRAND_MEDIUM_ORANGE,
            _BRAND_MEDIUM_GREEN,
            _BRAND_DARK_GRAY,
            _BRAND_DARK_BLUE,
            _BRAND_BRIGHT_BLUE,
            _BRAND_MEDIUM_PINK,
            _BRAND_DARK_ORANGE,
            _BRAND_LIGHT_PINK,
            _BRAND_DARK_GREEN,
        ],
        "dark": [
            _BRAND_MEDIUM_BLUE,
            _BRAND_MEDIUM_ORANGE,
            _BRAND_MEDIUM_GREEN,
            _BRAND_BRIGHT_GRAY,
            _BRAND_DARK_BLUE,
            _BRAND_BRIGHT_BLUE,
            _BRAND_MEDIUM_PINK,
            _BRAND_DARK_ORANGE,
            _BRAND_LIGHT_PINK,
            _BRAND_DARK_GREEN,
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
        "figure.facecolor": _LIGHT_BG_CANVAS,
        "axes.facecolor": _LIGHT_BG_PLOT,
        "text.color": _LIGHT_TEXT_PRIMARY,
        "axes.labelcolor": _LIGHT_TEXT_SECONDARY,
        "xtick.color": _LIGHT_TEXT_SECONDARY,
        "ytick.color": _LIGHT_TEXT_SECONDARY,
        "grid.color": _LIGHT_GRID,
        "axes.edgecolor": _LIGHT_AXIS_SPINE,
    },
    "dark": {
        "figure.facecolor": _DARK_BG_CANVAS,
        "axes.facecolor": _DARK_BG_PLOT,
        "text.color": _DARK_TEXT_PRIMARY,
        "axes.labelcolor": _DARK_TEXT_PRIMARY,
        "xtick.color": _DARK_TEXT_SECONDARY,
        "ytick.color": _DARK_TEXT_SECONDARY,
        "grid.color": _DARK_GRID,
        "axes.edgecolor": _DARK_AXIS_SPINE,
    },
}
