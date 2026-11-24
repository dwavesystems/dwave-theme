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

from importlib import resources
from typing import Any

import matplotlib
from cycler import cycler

from dwave.theme.core.catalog import PRESETS
from dwave.theme.core.colors import PALETTES, THEMES

STYLE_RESOURCE = resources.files(__package__) / "styles"


def _build_theme(theme: dict[str, str]) -> dict[str, str]:
    """Maps semantic core theme colors to Matplotlib ``rcParams`` keys."""
    return {
        "figure.facecolor": theme["bg_canvas"],
        "axes.facecolor": theme["bg_plot"],
        "text.color": theme["text_primary"],
        "axes.labelcolor": theme["axis_label"],
        "xtick.color": theme["text_secondary"],
        "ytick.color": theme["text_secondary"],
        "grid.color": theme["grid"],
        "axes.edgecolor": theme["axis_line"],
    }


def build_catalog() -> dict[str, Any]:
    """Constructs the dictionary of all available style components and presets.

    This mixes static ``.mplstyle`` files with dynamic dictionaries generated from the core color
    definitions.

    Returns:
        dict[str, Any]: A registry where keys are style names and values are either ``rcParams``
        dictionaries (components) or component-name lists (presets).
    """
    catalog: dict[str, Any] = {}

    if STYLE_RESOURCE.is_dir():
        for resource in STYLE_RESOURCE.iterdir():
            if resource.is_file() and resource.name.endswith(".mplstyle"):
                name = resource.name.removesuffix(".mplstyle")
                catalog[name] = _load_mplstyle_resource(resource)

    for name, settings in THEMES.items():
        catalog[f"theme-{name}"] = _build_theme(settings)

    for kind, variants in PALETTES.items():
        for variant, colors in variants.items():
            key = f"palette-{kind}-{variant}"
            catalog[key] = {"axes.prop_cycle": cycler(color=colors)}

    for name, components in PRESETS.items():
        catalog[name] = components.copy()

    return catalog


def _load_mplstyle_resource(resource: Any) -> dict[str, Any]:
    """Loads a packaged ``.mplstyle`` resource into an ``rcParams`` dictionary."""
    with resources.as_file(resource) as path:
        rc_params = matplotlib.rc_params_from_file(path, use_default_template=False)
        return dict(rc_params.items())
