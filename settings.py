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

import wx
import json
import os
import languages
from wx import DirDialog

# Configuration path
CONFIG_PATH = os.path.join(os.getenv('APPDATA'), 'DMYoutube2MP3', 'config.json')
# Language display names and language codes lists
language_list = languages.get_language_names()
language_codes = languages.list_languages()

# Translations
_ = languages.load_translations()

# Loading and saving configuration
def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_config(data):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# Settings dialog

class SettingsDialog(wx.Dialog):
    def __init__(self, parent=None):
        super().__init__(parent, title=_["Settings"], size=(450, 250))
        panel = wx.Panel(self)
        config = load_config()
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Language
        label_language = wx.StaticText(panel, label=_["Language:"])
        self.language_choice = wx.Choice(panel, choices=languages.get_language_names())
        self.language_choice.SetSelection(0)
        vbox.Add(label_language, flag=wx.Left | wx.Top, border=10)
        vbox.Add(self.language_choice, flag=wx.EXPAND | wx.Left | wx.Right, border=10)

        # Download folder
        folder_label = wx.StaticText(panel, label=_["Download folder:"])
        self.folder_ctrl = wx.TextCtrl(panel, value=config["general"].get("download_path", "default"))
        folder_btn = wx.Button(panel, label=_["Choose folder"])
        folder_btn.Bind(wx.EVT_BUTTON, self.on_choose_folder)
        vbox.Add(folder_label, flag=wx.LEFT | wx.TOP, border=10)
        vbox.Add(self.folder_ctrl, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        vbox.Add(folder_btn, flag=wx.LEFT | wx.TOP, border=10)

        # Save and Cancel buttons
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        save_btn = wx.Button(panel, label=_["Save Settings"])
        cancel_btn = wx.Button(panel, label=_["Cancel"])
        save_btn.Bind(wx.EVT_BUTTON, self.on_save)
        self.SetDefaultItem(save_btn)
        cancel_btn.Bind(wx.EVT_BUTTON, self.on_cancel)
        btn_sizer.Add(save_btn, flag=wx.RIGHT, border=10)
        btn_sizer.Add(cancel_btn)
        self.SetEscapeId(cancel_btn.GetId())
        vbox.Add(btn_sizer, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=15)

        panel.SetSizer(vbox)
        self.SetDefaultItem(save_btn)

    # Select folder event
    def on_choose_folder(self, event):
        with wx.DirDialog(self, _["Select download folder"]) as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                self.folder_ctrl.SetValue(dlg.GetPath())

    # Save settings event
    def on_save(self, event):
        language_code = language_codes[self.language_choice.GetSelection()]
        config = load_config()
        config["lang"]["selected_lang"] = language_code
        config["general"]["download_path"] = self.folder_ctrl.GetValue()
        save_config(config)
        wx.MessageBox(_["Settings saved. Restart app to apply changes."], _["Info"], wx.OK | wx.ICON_INFORMATION)
        self.EndModal(wx.ID_OK)

    # Cancel button event
    def on_cancel(self, event):
        self.EndModal(wx.ID_CANCEL)
