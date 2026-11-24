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

import re

import pytest

from dwave.theme.core.catalog import PRESETS, available_styles, resolve_styles
from dwave.theme.core.colors import PALETTES, THEMES, get_palettes

# A regex to ensure valid hex codes. Allows for optional transparency too, see:
# https://gist.github.com/lopspower/03fb1cc0ac9f32ef38f4
HEX_COLOR_PATTERN = re.compile(r"^#[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$")


@pytest.mark.parametrize("palette_type", ["qualitative", "sequential"])
@pytest.mark.parametrize("variant", ["light", "dark"])
def test_palettes_structure(palette_type, variant):
    """Ensure palettes exist and contain hex colors."""

    assert palette_type in PALETTES
    assert variant in PALETTES[palette_type]

    color_list = PALETTES[palette_type][variant]
    assert isinstance(color_list, list)
    assert len(color_list) > 0

    for color in color_list:
        assert isinstance(color, str)
        assert HEX_COLOR_PATTERN.match(color)


@pytest.mark.parametrize("variant", ["light", "dark"])
def test_themes_structure(variant):
    """Ensure semantic UI themes have the required keys and valid color values."""
    required_keys = [
        "bg_canvas",
        "bg_plot",
        "text_primary",
        "text_secondary",
        "axis_label",
        "grid",
        "axis_line",
    ]

    assert variant in THEMES
    theme_dict = THEMES[variant]

    for key in required_keys:
        assert key in theme_dict, f"Theme '{variant}' missing key '{key}'"

    assert len(theme_dict) == len(required_keys)

    for color_value in theme_dict.values():
        assert isinstance(color_value, str)
        assert HEX_COLOR_PATTERN.match(color_value)


def test_get_palettes_all_and_filtered():
    """Ensure ``get_palettes`` returns all palettes or filters by category."""
    all_palettes = get_palettes()
    assert len(all_palettes) == sum(len(v) for v in PALETTES.values())

    qual_palettes = get_palettes("qualitative")
    assert [label for label, _ in qual_palettes] == [
        "qualitative : light",
        "qualitative : dark",
    ]

    with pytest.raises(ValueError, match="Palette category 'unknown' not found"):
        get_palettes("unknown")


def test_resolve_styles_unpacks_presets_and_validates():
    """Ensure ``resolve_styles`` defaults to 'default', unpacks presets, and rejects bad inputs."""
    sample_catalog = {
        "base": {"base": 1},
        "typography": {"font": "sans"},
        "theme-light": {"bg": "#fff"},
        "palette-qualitative-light": {"colors": ["#000"]},
        "default": list(PRESETS["default"]),
        "nested": ["default"],
    }

    assert available_styles(sample_catalog) == sorted(sample_catalog.keys())
    assert resolve_styles(sample_catalog, ()) == [
        {"base": 1},
        {"font": "sans"},
        {"bg": "#fff"},
        {"colors": ["#000"]},
    ]
    assert resolve_styles(sample_catalog, ("base", "theme-light")) == [
        {"base": 1},
        {"bg": "#fff"},
    ]

    with pytest.raises(ValueError, match="Style 'missing' not found"):
        resolve_styles(sample_catalog, ("missing",))

    with pytest.raises(TypeError, match="cannot reference another preset"):
        resolve_styles(sample_catalog, ("nested",))
