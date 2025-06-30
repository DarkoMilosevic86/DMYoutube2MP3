# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.1.1] – 2025-06-30
### Fixed
- Language display names
---

## [1.1.0] – 2025-05-12
### Added
- Support for **YouTube playlists** – the app now detects playlist URLs and downloads each video individually.
- Visual **progress gauge** (`wx.Gauge`) that animates during download.
- Settings window allowing users to:
  - Choose application language
  - Set a custom download folder
- **Language localization system** with JSON files (`languages/sr_RS.json`, `en_US.json`, etc.)
- Automatic language detection based on system settings if no preference is set.
- Added:French, Italian, Spanish and Japanese language.
- Configuration saved in `config.json`.
- **Windows notifications** when a download starts and completes.
- **Download history** list with context menu actions:
  - Show in folder
  - Delete selected item
  - Using Enter and Delete keys to show selected item in folder, and delete selected item.
- "Clear history" button to remove the entire download history.

### Changed
- Improved download stability and error handling with `yt_dlp`.
- GUI layout enhancements and clearer status messages.

---

## [1.0.0] – 2025-05-07
### Added
- Initial release with basic functionality:
  - Download individual YouTube videos as MP3 using `yt_dlp` and `ffmpeg`.
  - Automatic detection of YouTube URLs from the clipboard.
  - Default download location: `C:\Users\<USERNAME>\Downloads\DM Youtube2mp3`
  - Simple GUI with URL input and download button.
  - Display of downloaded files in a list.
  - Download history saved to `history.json`.
  - Added Settings dialog for language selection and download folder selection.


