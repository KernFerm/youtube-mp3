import os
import shutil
from pydub import AudioSegment
import yt_dlp as youtube_dl

def check_ffmpeg():
    # Check if ffmpeg is in PATH
    ffmpeg_path = shutil.which("ffmpeg")
    if ffmpeg_path is None:
        print("FFmpeg is not installed or not found in PATH. Please install it and add it to PATH.")
        return False
    else:
        print(f"FFmpeg found at: {ffmpeg_path}")
        AudioSegment.ffmpeg = ffmpeg_path  # Set path for pydub to use ffmpeg
        return True

def download_audio():
    if not check_ffmpeg():
        return  # Stop if ffmpeg isn't found

    try:
        # Prompt for YouTube URL
        url = input("Enter the YouTube URL: ")

        # Download audio only using yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'downloaded_audio.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading and converting audio...")
            ydl.download([url])

        print("Download and conversion completed!")

    except Exception as e:
        print("An error occurred during the download or conversion process. Please try again.")
        print(f"Error details: {e}")

# Run the function
download_audio()
