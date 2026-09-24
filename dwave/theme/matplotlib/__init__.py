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

from typing import Any
import matplotlib.pyplot as plt
from dwave.theme.matplotlib.catalog import build_catalog
from dwave.theme.matplotlib.tools import show_palettes


__all__ = ["available_styles", "set_theme", "context", "show_palettes"]

_CATALOG = build_catalog()


def available_styles() -> list[str]:
    """Returns a sorted list of all valid style names (both presets and components).

    Returns:
        list[str]: A list of strings that can be passed to ``set_theme()`` or ``context()``.
    """
    return sorted(_CATALOG.keys())


def _resolve_styles(names: tuple[str, ...]) -> list[str | dict[str, Any]]:
    """Validates and unpacks style names.

    Args:
        names: A tuple of style names.

    Returns:
        resolved: A list of paths or ``rcParam`` dicts ready for matplotlib.

    Raises:
        ValueError: If a name is not found in the catalog.
    """
    resolved: list[str | dict[str, Any]] = []
    for name in names:
        if name not in _CATALOG:
            raise ValueError(
                f"Style '{name}' not found. Available: {available_styles()}"
            )

        val = _CATALOG[name]

        if isinstance(val, list):
            for item in val:
                resolved.append(_CATALOG[item])
        else:
            resolved.append(val)

    return resolved


def set_theme(*names: str) -> None:
    """Applies the D-Wave theme globally to the matplotlib session.

    This resets the existing matplotlib state to 'fast' before applying the requested styles to
    ensure a clean state.

    Args:
        *names: Variable length argument list of style names.
            If no arguments are provided, the 'default' preset is applied.

    Raises:
        ValueError: If a provided style name is not recognized.

    Examples:
        >>> # Apply the standard D-Wave look
        >>> import dwave.theme.matplotlib as dwave_theme
        >>> dwave_theme.set_theme()

        >>> # Apply the dark mode preset
        >>> dwave_theme.set_theme("dark")

        >>> # Compose specific components manually
        >>> # Base Layout + Dark UI + Qualitative Light Palette
        >>> dwave_theme.set_theme("base", "theme-dark", "palette-qualitative-light")
    """
    if not names:
        names = ("default",)

    styles_to_apply = _resolve_styles(names)

    plt.style.use("fast")
    plt.style.use(styles_to_apply)


def context(*names: str):
    """Context manager for temporary styling.

    Useful for generating a specific plot (e.g., for export) without changing the global state
    of the notebook or script.

    Args:
        *names: Variable length argument list of style names.
            If empty, uses 'default'.

    Returns:
        A matplotlib style context manager.

    Raises:
        ValueError: If a provided style name is not recognized.

    Examples:
        >>> # Global theme is dark
        >>> import dwave.theme.matplotlib as dwave_theme
        >>> import matplotlib.pyplot as plt
        ...
        >>> dwave_theme.set_theme("dark")
        >>> plt.plot(data)      # doctest: +SKIP
        >>>
        >>> # Temporarily switch to `presentation-light` preset for a slide export
        >>> with dwave_theme.context("presentation-light"):     # doctest: +SKIP
        ...     plt.plot(data)
        ...     plt.savefig("slide.png")
        >>>
        >>> # Global theme remains dark here
    """
    if not names:
        names = ("default",)

    styles_to_apply = _resolve_styles(names)

    return plt.style.context(styles_to_apply)
