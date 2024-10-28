# YouTube to MP3 Downloader

This Python script downloads audio from a YouTube video URL and converts it to an MP3 file at 192 kbps. It uses the `pytube` library for downloading YouTube videos and `pydub` for audio conversion with `ffmpeg`.

## Features

- Downloads audio from a YouTube video URL.
- Converts the audio to an MP3 file with a bitrate of 192 kbps.
- Automatically checks if `ffmpeg` is installed and sets its path for `pydub`.
- Cleans up temporary files after conversion.

## Requirements

- **Python** 3.6+
- **ffmpeg** (must be installed and added to PATH)
- **Python packages**:
  - `pytube`
  - `pydub`

## Installation

### 1. Install ffmpeg

#### Option A: Install with `winget` (Recommended for Windows Users)

Run this command in **Command Prompt** or **PowerShell** as Administrator:

```
winget install --id Gyan.FFmpeg -e --source winget
```

### Option B: Download and Manually Install

1. Download the latest `ffmpeg` build from [ffmpeg.org](https://ffmpeg.org/download.html) or [gyan.dev](https://www.gyan.dev/ffmpeg/builds/).
2. Extract the files and add the `bin` directory (e.g., `C:\ffmpeg\bin`) to your system PATH.

- Verify `ffmpeg` installation by running:

```
ffmpeg -version
```

### 2. Install Python Packages

- Install the required packages by running:

```
pip install pytube pydub
```

## Usage

1. `Clone` or `download` this repository.
2. Run the script:

```
python main.py
```

- Enter the YouTube video URL when prompted.

The script will download the audio from the specified YouTube URL, convert it to MP3 format at 192 kbps, and save it in the current directory with the video title as the filename.

## Example

```
$ python main.py
FFmpeg found at: C:\path\to\ffmpeg.exe
Enter the YouTube URL: https://www.youtube.com/watch?v=example
Downloading 'Video Title'...
Converting to MP3 with 192 kbps bitrate...
Download and conversion completed!
MP3 file saved as: Video_Title_192kbps.mp3
```

## Troubleshooting

- **FFmpeg Not Found**: If you see the message `FFmpeg is not installed or not found in PATH`. Please install it and add it to PATH., ensure that `ffmpeg` is installed and correctly added to your PATH.

## Notes

- Ensure `ffmpeg` is installed and added to your system PATH so `pydub` can locate it.

- If installed with `winget`, `ffmpeg` may be located at `C:\Users\<username>\AppData\Local\Microsoft\WinGet\Links`.

# LICENSE

- ## ***This project is proprietary and all rights are reserved by the author.***
- ## ***Unauthorized copying, distribution, or modification of this project is strictly prohibited.***
- ## ***Unless You have written permission from the Developer or the FNBUBBLES420 ORG.***




















