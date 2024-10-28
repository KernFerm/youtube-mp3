from pytube import YouTube
from pydub import AudioSegment
import os
import shutil

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
        
        # Downloading and displaying video title
        yt = YouTube(url)
        print(f"Downloading '{yt.title}'...")

        # Fetch audio stream and download
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_file = audio_stream.download(filename="downloaded_audio")

        # Convert to MP3 format with 192kbps
        mp3_filename = f"{yt.title.replace(' ', '_')}_192kbps.mp3"
        print("Converting to MP3 with 192 kbps bitrate...")
        audio = AudioSegment.from_file(audio_file)
        audio.export(mp3_filename, format="mp3", bitrate="192k")

        # Clean up the original downloaded file
        os.remove(audio_file)

        # Confirm completion and file location
        print(f"Download and conversion completed!\nMP3 file saved as: {mp3_filename}")

    except Exception as e:
        print("An error occurred during the download or conversion process. Please try again.")
        print(f"Error details: {e}")

# Run the function
download_audio()
