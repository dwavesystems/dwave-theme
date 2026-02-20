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

from dwave.theme.core.colors import PALETTES, THEMES


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

    for i, color in enumerate(color_list):
        assert isinstance(color, str)
        assert HEX_COLOR_PATTERN.match(color)


@pytest.mark.parametrize("variant", ["light", "dark"])
def test_themes_structure(variant):
    """Ensure UI themes have the required keys and valid color values."""
    required_keys = [
        "figure.facecolor",
        "axes.facecolor",
        "text.color",
        "axes.labelcolor",
        "xtick.color",
        "ytick.color",
        "grid.color",
        "axes.edgecolor",
    ]

    assert variant in THEMES
    theme_dict = THEMES[variant]

    for key in required_keys:
        assert key in theme_dict, f"Theme '{variant}' missing key '{key}'"

    assert len(theme_dict) == len(required_keys)

    for key, color_value in theme_dict.items():
        assert isinstance(color_value, str)
        assert HEX_COLOR_PATTERN.match(color_value)
