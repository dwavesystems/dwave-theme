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

from pathlib import Path
from typing import Any
from cycler import cycler
from dwave.theme.core.colors import PALETTES, THEMES


STYLE_DIR = Path(__file__).parent / "styles"


def build_catalog() -> dict[str, Any]:
    """Constructs the dictionary of all available style components.

    This mixes static `.mplstyle` files with dynamic dictionaries generated from the core color
    definitions.

    Returns:
        dict[str, Any]: A registry where keys are style names and values are either `Path` objects
            (to `.mplstyle` files) or dictionaries (`rcParams`).
    """
    catalog = {}

    if STYLE_DIR.exists():
        for path in STYLE_DIR.glob("*.mplstyle"):
            catalog[path.stem] = path

    for name, settings in THEMES.items():
        catalog[f"theme-{name}"] = settings

    for kind, variants in PALETTES.items():
        for variant, colors in variants.items():
            key = f"palette-{kind}-{variant}"
            catalog[key] = {"axes.prop_cycle": cycler(color=colors)}

    # Define presets
    catalog["default"] = [
        "base",
        "typography",
        "theme-light",
        "palette-qualitative-light",
    ]

    catalog["dark"] = ["base", "typography", "theme-dark", "palette-qualitative-dark"]

    catalog["presentation"] = [
        "base",
        "typography",
        "presentation",
        "theme-light",
        "palette-qualitative-light",
    ]

    catalog["presentation-dark"] = [
        "base",
        "typography",
        "presentation",
        "theme-dark",
        "palette-qualitative-dark",
    ]

    return catalog
