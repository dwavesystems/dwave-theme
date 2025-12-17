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

from dwave.theme.core.colors import PALETTES, THEMES


def test_palettes_structure():
    """Ensure palettes are defined correctly."""
    assert "qualitative" in PALETTES
    assert "light" in PALETTES["qualitative"]
    assert "dark" in PALETTES["qualitative"]

    light_palette = PALETTES["qualitative"]["light"]
    assert isinstance(light_palette, list)
    assert len(light_palette) > 0
    assert light_palette[0].startswith("#")


def test_themes_structure():
    """Ensure UI themes have the required keys."""
    required_keys = ["figure.facecolor", "axes.facecolor", "text.color"]

    for variant in ["light", "dark"]:
        assert variant in THEMES
        theme_dict = THEMES[variant]

        for key in required_keys:
            assert key in theme_dict, f"Theme '{variant}' missing key '{key}'"
