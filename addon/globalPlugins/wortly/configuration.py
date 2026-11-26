# A part of the Wortly add-on for NVDA
# Copyright (C) 2026 Oleksandr Gryshchenko <grisov.nvaccess@mailgw.com>
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

"""The name and the summary of the add-on."""

from typing import Any, cast

import addonHandler

# The manifest of the add-on has no type annotations
_addon = cast(Any, addonHandler).getCodeAddon()
ADDON_NAME: str = _addon.name
ADDON_SUMMARY: str = _addon.manifest["summary"]
