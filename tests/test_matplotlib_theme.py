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

import pytest
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import Cycler

from dwave.theme.core.colors import (
    _LIGHT_BG_PLOT,
    _DARK_BG_PLOT,
    _DARK_TEXT_PRIMARY,
    PALETTES,
    THEMES,
)
from dwave.theme.matplotlib import available_styles, set_theme, context, show_palettes
from dwave.theme.matplotlib.catalog import build_catalog


def test_catalog_loads_static_files():
    """Verify ``.mplstyle`` files are discovered and loaded into the catalog."""
    catalog = build_catalog()
    mpl_static = ["base", "presentation", "transparent", "typography"]

    for style in mpl_static:
        assert style in catalog, f"Style '{style}' is missing from the catalog."


def test_catalog_loads_themes():
    """Verify themes are correctly loaded into the catalog."""
    catalog = build_catalog()

    for theme_name in THEMES.keys():
        assert f"theme-{theme_name}" in catalog, (
            f"Theme theme-{theme_name} failed to load."
        )


def test_catalog_loads_palettes():
    """Verify all palettes are loaded with valid Matplotlib Cyclers."""
    catalog = build_catalog()

    for kind, variants in PALETTES.items():
        for variant in variants.keys():
            expected_key = f"palette-{kind}-{variant}"

            assert expected_key in catalog, f"Palette {expected_key} failed to load."

            palette_dict = catalog[expected_key]
            assert "axes.prop_cycle" in palette_dict, (
                f"Palette {expected_key} missing color cycler."
            )

            prop_cycle = palette_dict["axes.prop_cycle"]
            assert isinstance(prop_cycle, Cycler), "Expected a Cycler object."


def _preset_names():
    """Return every preset name in the catalog."""
    return [name for name, val in build_catalog().items() if isinstance(val, list)]


@pytest.mark.parametrize("preset_name", _preset_names())
def test_presets_reference_valid_components(preset_name):
    """Ensure each preset references existing components and not another preset."""
    catalog = build_catalog()
    presets = set(_preset_names())

    for component in catalog[preset_name]:
        assert component in catalog, (
            f"Preset '{preset_name}' relies on component '{component}', "
            f"but '{component}' is not in the catalog."
        )
        assert component not in presets, (
            f"Preset '{preset_name}' references '{component}', which is also a "
            f"preset; presets must only reference components."
        )


@pytest.mark.parametrize("preset_name", _preset_names())
def test_set_theme_applies_every_preset(preset_name):
    """Verify every preset can be applied via ``set_theme()`` without error."""
    set_theme(preset_name)


def test_available_styles_returns_sorted_list():
    """Test that ``available_styles()`` returns a sorted list of style names."""
    styles = available_styles()
    assert isinstance(styles, list)
    assert "default" in styles
    assert styles == sorted(styles)


def test_set_theme_defaults():
    """Test that ``set_theme()`` with no args applies the default preset."""
    set_theme()
    assert plt.rcParams["figure.facecolor"] == _LIGHT_BG_PLOT


def test_set_theme_dark_preset():
    """Test applying a preset via ``set_theme()`` works."""
    set_theme("dark")
    assert plt.rcParams["figure.facecolor"] == _DARK_BG_PLOT


def test_set_theme_invalid_name():
    """Test that a ValueError is raised for bad style names."""
    expected_error = "Style 'non_existent_style' not found"
    with pytest.raises(ValueError, match=expected_error):
        set_theme("non_existent_style")


def test_set_theme_composition():
    """Test mixing a static style (base) and a theme component."""
    set_theme("base", "theme-light")

    assert plt.rcParams["axes.grid"] is False
    assert plt.rcParams["figure.facecolor"] == _LIGHT_BG_PLOT


def test_transparent_style_application():
    """Test that the transparent component sets facecolors to none."""
    set_theme("transparent")

    assert plt.rcParams["figure.facecolor"] == "none"
    assert plt.rcParams["axes.facecolor"] == "none"
    assert plt.rcParams["savefig.facecolor"] == "none"


def test_transparent_composition():
    """
    Test that transparency layers correctly on top of a color theme.
    """
    set_theme("dark", "transparent")
    assert plt.rcParams["figure.facecolor"] == "none"
    assert plt.rcParams["text.color"] == _DARK_TEXT_PRIMARY


def test_context_manager_isolation():
    """Ensure context manager applies styles temporarily."""
    set_theme("default")
    original_bg = plt.rcParams["figure.facecolor"]

    with context("dark"):
        assert plt.rcParams["figure.facecolor"] == _DARK_BG_PLOT

    # check revert after context use
    assert plt.rcParams["figure.facecolor"] == original_bg


def test_show_palettes_runs_without_error(mocker):
    """Smoke test the palette visualizer."""
    mpl.use("Agg")
    mock_show = mocker.patch("matplotlib.pyplot.show")

    show_palettes()

    mock_show.assert_called_once()


def test_show_palettes_filtered(mocker):
    """Test filtering by category."""
    mpl.use("Agg")
    mocker.patch("matplotlib.pyplot.show")

    show_palettes("qualitative")


def test_show_palettes_invalid_category():
    """Test invalid category raises error."""
    with pytest.raises(ValueError):
        show_palettes("non_existent_category")
