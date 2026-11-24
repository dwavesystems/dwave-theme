# Copyright 2026 D-Wave
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

"""Shared preset definitions and style catalog resolution helpers."""

from collections.abc import Mapping
from typing import Any, TypeVar

T = TypeVar("T")

PRESETS: dict[str, list[str]] = {
    "default": [
        "base",
        "typography",
        "theme-light",
        "palette-qualitative-light",
    ],
    "light": [
        "base",
        "typography",
        "theme-light",
        "palette-qualitative-light",
    ],
    "dark": [
        "base",
        "typography",
        "theme-dark",
        "palette-qualitative-dark",
    ],
    "presentation-light": [
        "base",
        "typography",
        "presentation",
        "theme-light",
        "palette-qualitative-light",
    ],
    "presentation-dark": [
        "base",
        "typography",
        "presentation",
        "theme-dark",
        "palette-qualitative-dark",
    ],
}


def available_styles(catalog: Mapping[str, Any]) -> list[str]:
    """Returns a sorted list of all valid style names in ``catalog``.

    Args:
        catalog: Mapping of style names to backend style objects or preset component lists.

    Returns:
        list[str]: Sorted style names present in ``catalog``.
    """
    return sorted(catalog.keys())


def resolve_styles(
    catalog: Mapping[str, T | list[str]],
    names: tuple[str, ...],
) -> list[T]:
    """Validates and unpacks style names (presets and components) from ``catalog``.

    Args:
        catalog: Mapping of style names to backend style objects or preset component lists.
        names: Style names requested by the caller. Defaults to ``("default",)`` if empty.

    Returns:
        list[T]: Flat list of resolved backend style components.

    Raises:
        ValueError: If a requested style name is not found in ``catalog``.
        TypeError: If a preset references another preset instead of a component.
    """
    if not names:
        names = ("default",)

    resolved: list[T] = []
    for name in names:
        if name not in catalog:
            raise ValueError(
                f"Style '{name}' not found. Available: {available_styles(catalog)}"
            )

        val = catalog[name]
        if isinstance(val, list):
            for item in val:
                component = catalog[item]
                if isinstance(component, list):
                    raise TypeError(
                        f"Preset '{name}' cannot reference another preset '{item}'."
                    )
                resolved.append(component)
        else:
            resolved.append(val)

    return resolved
