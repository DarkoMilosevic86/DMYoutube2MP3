# -*- coding: utf-8 -*-
#
# DM Youtube2MP3 – YouTube to MP3 downloader
#
# Copyright (C) 2025  Darko MILOŠEVIĆ <daremc86@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#

import os
import json
import locale
from babel import Locale

LANG_FOLDER = os.path.join(os.path.dirname(__file__), 'languages')
DEFAULT_LANG = 'en_US'
CONFIG_PATH = os.path.join(os.getenv('APPDATA'), 'DMYoutube2MP3', 'config.json')

def list_languages():
    """Returns list of available language codes from the languages folder."""
    return [f.replace('.json', '') for f in os.listdir(LANG_FOLDER) if f.endswith('.json')]

def get_system_lang():
    """Returns the system language code (e.g. 'sr_RS') or None if not available."""
    sys_lang, _ = locale.getdefaultlocale()
    return sys_lang

def get_selected_language():
    """Reads config and determines which language to use."""
    if not os.path.exists(CONFIG_PATH):
        return DEFAULT_LANG

    try:
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            config = json.load(f)
        lang = config.get("lang", {}).get("selected_lang", "default")
        if lang == "default":
            system_lang = get_system_lang()
            if system_lang in list_languages():
                return system_lang
            return DEFAULT_LANG
        elif lang in list_languages():
            return lang
        else:
            return DEFAULT_LANG
    except Exception:
        return DEFAULT_LANG

def load_translations():
    """Loads the translation dictionary for the selected language."""
    lang_code = get_selected_language()
    path = os.path.join(LANG_FOLDER, f"{lang_code}.json")

    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        fallback = os.path.join(LANG_FOLDER, f"{DEFAULT_LANG}.json")
        with open(fallback, 'r', encoding='utf-8') as f:
            return json.load(f)

def get_language_names():
    language_codes = list_languages()
    language_names = []
    for language_code in language_codes:
        locale_lang = Locale.parse(language_code)
        lang_name = locale_lang.get_display_name().capitalize()
        language_names.append(lang_name)
    return language_names
