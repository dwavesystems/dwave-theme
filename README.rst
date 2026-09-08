============
D-Wave Theme
============

.. start_theme_about

``dwave-theme`` is a centralized theme and configuration package for creating
unified, D-Wave-branded user interfaces and visualizations across D-Wave
projects. It provides:

*   A central repository of D-Wave brand color palettes (qualitative,
    sequential) with light and dark variants.
*   Ready-to-use `matplotlib <https://matplotlib.org>`_ style presets, such as
    ``default``, ``dark``, and ``presentation-light``, as well as composable
    style components (base layout, typography, themes, and palettes) for
    building custom looks.

.. code-block:: python

    import matplotlib.pyplot as plt
    import dwave.theme.matplotlib as dwave_theme

    # List all available presets and components
    dwave_theme.available_styles()

    # Apply the standard D-Wave look globally
    dwave_theme.set_theme()

    # Or apply the dark preset
    dwave_theme.set_theme("dark")

    # Temporarily switch styles for a specific figure
    with dwave_theme.context("presentation-light"):
        plt.plot([1, 2, 3])
        plt.savefig("slide.png")

    # Preview the available color palettes
    dwave_theme.show_palettes()

.. end_theme_about

Installation
============

Installation from `PyPI <https://pypi.org/project/dwave-theme>`_:

.. code-block:: bash

    pip install dwave-theme

During package development, it is often convenient to use an editable install:

.. code-block:: bash

    pip install --editable .

Testing
=======

All code should be thoroughly tested and all pull requests should include
tests.

To run the tests, first install the package using an editable install as
described above, along with the test dependencies:

.. code-block:: bash

    pip install --group test

The tests can then be run with `pytest <https://docs.pytest.org>`_:

.. code-block:: bash

    pytest tests/

Versioning
==========

This package follows `semantic versioning <https://semver.org>`_: breaking
changes to the public API are only introduced in major releases.

License
=======

Released under the Apache License 2.0. See LICENSE file.

Contributing
============

Ocean's `contributing guide
<https://docs.dwavequantum.com/en/latest/ocean/contribute.html>`_
has guidelines for contributing to Ocean packages.

Release Notes
-------------

``dwave-theme`` makes use of `reno <https://docs.openstack.org/reno/>`_ to manage
its release notes.

When making a contribution to ``dwave-theme`` that will affect users, create a
new release note file by running:

.. code-block:: bash

    reno new your-short-descriptor-here

You can then edit the file created under ``releasenotes/notes/``. Remove any
sections not relevant to your changes. Commit the file along with your changes.

See reno's `user guide <https://docs.openstack.org/reno/latest/user/usage.html>`_
for details.
