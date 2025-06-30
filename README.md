# DMYoutube2MP3

**DMYoutube2MP3** is a free and open-source Windows desktop application for downloading audio from YouTube videos and converting it to high-quality MP3 files using `yt-dlp` and `ffmpeg`.  
It features a lightweight GUI built with `wxPython`, automatic clipboard detection, native system notifications, and persistent download history with context menu options.

---

## 🔧 Features

- 🎞️ Paste YouTube URLs manually or from clipboard
- 🔊 Extract audio and convert to **MP3 (192kbps)** using `yt-dlp` and `ffmpeg`
- 🔔 Native Windows notifications using `wx.adv.NotificationMessage`
- 📋 Persistent download history with:
  - Right-click context menu (`Show in Folder`, `Delete`)
  - Delete support via keyboard (`Delete` key)
  - Enter or NumPad Enter, opens selected item in Windows Explorer
- 📁 Automatically saves files to:
`C:\Users\yourusername\Downloads\DMYoutube2MP3`
- Multi lingual support

## 📚DMYoutube2MP3 documentation

- [About DMYoutube2MP3](docs/index.md)
- [Installation](docs/installation.md)
- [Using DMYoutube2MP3](docs/usage.md)
- [Frequently asked questions](docs/faq.md)
- [DMYoutube2MP3 localization](docs/localization.md)
- [Contribution to DMYoutube2MP3](docs/contributing.md)

## 🚀 Building from source
> Python 3.10+ is recommended.

### 1. Clone the repository:

```bash
git clone https://github.com/DarkoMilosevic86/DMYoutube2MP3.git
cd DMYoutube2MP3
```

### 2. Build the source code

- To build the source code, make sure Python 3.10+ is installed on your computer.
- Run `build.bat` to build the DMYoutube2MP3 from source.
#### Important note!
To build the DMYoutube2MP3 from the source code, you must download ffmpeg binary and copy the file ffmpeg.exe to the main repository folder

## 🤝 Contributing

We welcome contributions to DM Youtube2MP3! If you'd like to report a bug, suggest a feature, or contribute code, please check out our [CONTRIBUTING.md](CONTRIBUTING.md) guide.