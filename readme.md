# Bubbles The Dev Youtube To MP3 Downloader

This Python script downloads audio from a YouTube video URL or playlist and converts it to MP3 files at 192 kbps. It utilizes the `yt-dlp` library for downloading, `pydub` for audio conversion, and `mutagen` for embedding metadata. The script is protected with `pyarmor` for added security.

## Features

- Downloads audio from a YouTube video or playlist.
- Converts the audio to MP3 files with a bitrate of 192 kbps.
- Embeds metadata (title, artist, album) into the MP3 files.
- Automatically checks if `ffmpeg` is installed and configures its path for `pydub`.
- Secures the script using `pyarmor`.
- Cleans up temporary files after conversion.

## Requirements

- **Python** 3.11 [Python 3.11.6 Installer](https://github.com/KernFerm/Py3.11.6installer)
- `python batch file` to install python
- **ffmpeg** (must be installed and added to PATH)
- **Python packages**:
  - `yt-dlp`
  - `pydub`
  - `mutagen`
  - `pyarmor` (for script protection)

## Discord

If you have any issues, join our [Discord](https://www.discord.fnbubbles420.org/invite) - Fnbubbles420 Org Community.  
- Head to the channel `free-music`
- Ping `Bubbles` for support.

### Project Link

- [Pre-Release](https://github.com/KernFerm/Bubbles_The_Dev_Youtube_To_MP3/releases/tag/youtube-to-mp3)

---

## Installation

### 1. Install ffmpeg

#### Option A: Install with `winget` (Recommended for Windows Users)

```
winget install --id Gyan.FFmpeg -e --source winget
```

Option B: Download and Manually Install
- Download the latest ffmpeg build from ffmpeg.org or gyan.dev.
- Extract the files and add the bin directory (e.g., C:\ffmpeg\bin) to your system PATH.
- Verify ffmpeg installation by running:
```
ffmpeg -version
```
## if winget doesnt work try choco

Chocolatey is another package manager for Windows, similar to winget. You can use it to install FFmpeg and other software if winget is failing.

To install FFmpeg using Chocolatey, follow these steps:

Install Chocolatey if you haven't already:

Open an elevated Command Prompt (right-click on Command Prompt and select "Run as Administrator").
Run the following command to install Chocolatey:

```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

After Chocolatey is installed, use the following command to install FFmpeg:

```
choco install ffmpeg
```

### 2. Install Python Packages
```
pip install yt-dlp pydub mutagen pyarmor
```

### Execute the script: 
- make sure to `cd` the location before running:
```
python main.py
```
- Follow the prompts to choose between downloading a single track or a playlist, and enter the YouTube URL when prompted.

### Example Usage

```
$ python main.py
FFmpeg found at: C:\path\to\ffmpeg.exe
Do you want to download a single track or a playlist? (Enter 'track' or 'playlist'): playlist
Enter the YouTube URL: https://www.youtube.com/playlist?list=example
Downloading and converting audio...
Processing metadata for Track Title...
Download and conversion completed!
MP3 files saved in: downloaded_audio/
```

## Troubleshooting

- **FFmpeg Not Found**: If you see the message FFmpeg is `not installed` or `not found in PATH`, please ensure that ffmpeg is installed and correctly added to your PATH.
- Dependency Issues: Ensure all required Python packages, including pyarmor, are installed.

## LICENSE

This project is proprietary and all rights are reserved by the author.
Unauthorized copying, distribution, or modification of this project is strictly prohibited.
You must have written permission from the developer or the FNBUBBLES420 ORG to use or distribute this project.
