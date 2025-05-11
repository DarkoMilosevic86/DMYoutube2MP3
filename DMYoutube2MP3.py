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
import os
import pyperclip
from pathlib import Path
import json
import threading
import getpass
import wx.adv
import yt_dlp
import subprocess
import shutil
import languages

# Set download path and config path
USERNAME = getpass.getuser()
HISTORY_FILE = os.path.join(os.getenv('APPDATA'), 'DMYoutube2MP3', "history.json")
config_path = os.path.join(os.getenv('APPDATA'), 'DMYoutube2MP3', 'config.json')
os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
if not os.path.exists(config_path):
    shutil.copy2(os.path.join(os.getcwd(), 'config.json'), config_path)
with open(config_path, 'r', encoding='utf-8') as file:
    config = json.load(file)
if config["general"]["download_path"] == "default":
    DOWNLOAD_FOLDER = Path(f"C:/Users/{USERNAME}/Downloads/DM Youtube2mp3")
else:
    DOWNLOAD_FOLDER = Path(f"{config["general"]["download_path"]}")
DOWNLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

# Translations
_ = languages.load_translations()

# Windows notifications
def send_notification(title, message, parent=None):
    notifyer = wx.adv.NotificationMessage(title, message, parent, flags=wx.ICON_INFORMATION)
    notifyer.Show(timeout=5000)

# History saving
def save_to_history(title, filename):
    history = load_history()
    history.append({"title": title, "file": filename})
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2)

# Loading history
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# Download and convert to MP3
def download_with_ytdlp(url, callback=None):
    try:
        send_notification("DM Youtube2MP3", _["Download started..."], parent=None)

        is_playlist = 'playlist' in url or 'list=' in url

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': str(DOWNLOAD_FOLDER / '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': True,
            'noplaylist': False,
            'ignoreerrors': True,
            'ffmpeg_location': str(Path(__file__).parent),
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

            if 'entries' in info:  # Playlist
                for entry in info['entries']:
                    title = entry.get('title', 'Unknown title')
                    mp3_path = DOWNLOAD_FOLDER / f"{title}.mp3"
                    save_to_history(title, str(mp3_path))
            else:  # Single video
                title = info.get('title', 'Unknown title')
                mp3_path = DOWNLOAD_FOLDER / f"{title}.mp3"
                save_to_history(title, str(mp3_path))

        wx.CallAfter(send_notification, "DM Youtube2MP3", _["Download finished"], wx.GetTopLevelWindows()[0])
        if callback:
            callback(f"{_['Finished:']} {info.get('title', 'Multiple')}")
    except Exception as e:
        send_notification(_["Download Error"], f"{_['Unsuccessfull']}: {str(e)}")
        if callback:
            callback(f"Error: {str(e)}")

# GUI application
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="DM Youtube2MP3", size=(600, 400))
        panel = wx.Panel(self)
        self.Bind(wx.EVT_CLOSE, self.on_close)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.url_ctrl = wx.TextCtrl(panel)
        self.url_ctrl.Bind(wx.EVT_TEXT, self.on_text_changed)
        vbox.Add(self.url_ctrl, flag=wx.EXPAND | wx.ALL, border=10)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        paste_btn = wx.Button(panel, label=_["Paste from Clipboard"])
        paste_btn.Bind(wx.EVT_BUTTON, self.on_paste)
        hbox.Add(paste_btn, flag=wx.RIGHT, border=5)

        self.download_btn = wx.Button(panel, label=_["Download"])
        self.download_btn.Bind(wx.EVT_BUTTON, self.on_download)
        self.download_btn.Enable(False)
        hbox.Add(self.download_btn)

        vbox.Add(hbox, flag=wx.LEFT | wx.BOTTOM, border=10)

        self.history_list = wx.ListBox(panel)
        self.history_list.Bind(wx.EVT_CONTEXT_MENU, self.on_context_menu)
        self.history_list.Bind(wx.EVT_KEY_UP, self.on_press_del_key)
        self.history_list.Bind(wx.EVT_LEFT_DCLICK, self.on_double_click)
        vbox.Add(self.history_list, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        clear_btn = wx.Button(panel, label=_["Clear history"])
        clear_btn.Bind(wx.EVT_BUTTON, self.on_clear_history)
        vbox.Add(clear_btn, flag=wx.LEFT | wx.BOTTOM, border=10)

        self.status = wx.StaticText(panel, label="")
        vbox.Add(self.status, flag=wx.ALL, border=10)
        settings_btn = wx.Button(panel, label=_["Settings"])
        settings_btn.Bind(wx.EVT_BUTTON, self.on_open_settings)
        vbox.Add(settings_btn, flag=wx.LEFT | wx.BOTTOM, border=10)
        panel.SetSizer(vbox)
        self.load_history_into_list()
        history = load_history()
        if len(history) > 0:
            self.history_list.SetSelection(0)

    def on_paste(self, event):
        url = pyperclip.paste()
        if "youtube.com/watch" in url or "youtu.be" in url:
            self.url_ctrl.SetValue(url)
        else:
            self.status.SetLabel(_["Clipboard does not contains a valid YouTube link."])

    def on_download(self, event):
        url = self.url_ctrl.GetValue()
        if not url:
            self.status.SetLabel(_["Please enter a YouTube URL."])
            return
        self.status.SetLabel(_["Download in progress..."])
        threading.Thread(target=download_with_ytdlp, args=(url, self.update_status), daemon=True).start()

    def on_text_changed(self, event):
        url = self.url_ctrl.GetValue().strip()
        self.download_btn.Enable(bool(url))

    def on_context_menu(self, event):
        selection = self.history_list.GetSelection()
        if selection == wx.NOT_FOUND:
            return
        context_menu = wx.Menu()
        show_item = context_menu.Append(wx.ID_ANY, _["Show in Folder"])
        delete_item = context_menu.Append(wx.ID_ANY, _["Delete"])
        self.Bind(wx.EVT_MENU, lambda evt:self.on_show_in_folder(selection), show_item)
        self.Bind(wx.EVT_MENU, lambda evt:self.on_delete(selection), delete_item)
        self.PopupMenu(context_menu)
        context_menu.Destroy()

    def update_status(self, message):
        wx.CallAfter(self.status.SetLabel, message)
        wx.CallAfter(self.load_history_into_list)

    def load_history_into_list(self, event=None):
        self.history_list.Clear()
        history = load_history()
        for item in history:
            self.history_list.Append(item["title"])

    def on_clear_history(self, event):
        if os.path.exists(HISTORY_FILE):
            os.remove(HISTORY_FILE)
        self.load_history_into_list()
        self.status.SetLabel(_["History cleared."])

    def on_show_in_folder(self, index):
        history = load_history()
        item = history[index]
        item_path = item["file"]
        if os.path.exists(item_path):
            subprocess.Popen(['explorer', '/select,', os.path.normpath(item_path)])
        else:
            self.status.SetLabel("File not found.")

    def on_delete(self, index):
        history = load_history()
        del history[index]
        try:
            with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
                json.dump(history, f, indent=2)
            self.load_history_into_list()
            if len(history) > 0:
                self.history_list.SetSelection(index)
            self.status.SetLabel(_["Item deleted."])
        except Exception as e:
            self.status.SetLabel(f"{_["Error while clearing history"]}: {e}")
            return

    def on_close(self, event):
        self.Destroy()
        wx.GetApp().ExitMainLoop()

    def on_press_del_key(self, event):
        key_code = event.GetKeyCode()
        if key_code == wx.WXK_DELETE:
            self.on_delete(self.history_list.GetSelection())
        if key_code == wx.WXK_NUMPAD_ENTER or key_code == wx.WXK_RETURN:
            self.on_show_in_folder(self.history_list.GetSelection())
    def on_open_settings(self, event):
        from settings import SettingsDialog
        dlg = SettingsDialog(self)
        dlg.ShowModal()
        dlg.Destroy()

    def on_double_click(self, event):
        self.on_show_in_folder(self.history_list.GetSelection())


# Running the app
if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
