# A part of the Wortly add-on for NVDA
# Copyright (C) 2026 Oleksandr Gryshchenko <grisov.nvaccess@mailgw.com>
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

"""Helps to learn German words with flashcards and spaced repetition:
speaks a word in Ukrainian and checks the German word typed by the user.
"""

from collections.abc import Callable
from typing import Any

import addonHandler
import globalPluginHandler
from logHandler import log

from .configuration import ADDON_SUMMARY

try:
	addonHandler.initTranslation()
except addonHandler.AddonError:
	log.warning("Unable to init translations. This may be because the addon is running from NVDA scratchpad.")
_: Callable[[str], str]


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	"""The entry point of the add-on in NVDA."""

	# The category of the commands of the add-on in the NVDA "Input gestures" dialog
	scriptCategory: str = ADDON_SUMMARY

	def __init__(self, *args: Any, **kwargs: Any) -> None:
		"""Initialize the add-on when NVDA starts or the plugins are reloaded."""
		super().__init__(*args, **kwargs)
