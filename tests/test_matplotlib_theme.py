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

from dwave.theme.core.colors import _LIGHT_BG_PLOT, _DARK_BG_PLOT, _DARK_TEXT_PRIMARY
from dwave.theme.matplotlib import available_styles, set_theme, context, show_palettes
from dwave.theme.matplotlib.catalog import build_catalog


def test_catalog_builds_correctly():
    """Verify the catalog loads static files, themes, and palettes."""
    catalog = build_catalog()

    assert "base" in catalog
    assert "typography" in catalog

    assert "theme-light" in catalog
    assert "theme-dark" in catalog

    assert "palette-qualitative-light" in catalog

    assert "default" in catalog
    assert isinstance(catalog["default"], list)


def test_available_styles_returns_sorted_list():
    """Test that `available_styles()` returns a sorted list of style names."""
    styles = available_styles()
    assert isinstance(styles, list)
    assert "default" in styles
    assert styles == sorted(styles)


def test_set_theme_defaults():
    """Test that `set_theme()` with no args applies the default preset."""
    set_theme()
    assert plt.rcParams["figure.facecolor"] == _LIGHT_BG_PLOT


def test_set_theme_dark_preset():
    """Test applying a preset works."""
    set_theme("dark")
    assert plt.rcParams["figure.facecolor"] == _DARK_BG_PLOT


def test_set_theme_invalid_name():
    """Test that a ValueError is raised for bad style names."""
    with pytest.raises(ValueError) as excinfo:
        set_theme("non_existent_style")

    assert "Style 'non_existent_style' not found" in str(excinfo.value)


def test_set_theme_composition():
    """Test mixing a static style (base) and a theme component."""
    set_theme("base", "theme-light")

    assert plt.rcParams["axes.grid"] is False
    assert plt.rcParams["figure.facecolor"] == _LIGHT_BG_PLOT


def test_catalog_has_transparent():
    """Ensure the transparent component is discovered."""
    catalog = build_catalog()
    assert "transparent" in catalog


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
    """
    Smoke test the palette visualizer.
    """
    mpl.use("Agg")

    mock_show = mocker.patch("matplotlib.pyplot.show")

    try:
        show_palettes()
    except Exception as e:
        pytest.fail(f"show_palettes raised an exception: {e}")

    mock_show.assert_called_once()


def test_show_palettes_filtered(mocker):
    """Test filtering by category."""
    mpl.use("Agg")
    mocker.patch("matplotlib.pyplot.show")

    try:
        show_palettes("qualitative")
    except Exception as e:
        pytest.fail(f"show_palettes('qualitative') raised: {e}")


def test_show_palettes_invalid_category():
    """Test invalid category raises error."""
    with pytest.raises(ValueError):
        show_palettes("non_existent_category")
