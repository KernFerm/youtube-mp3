import os
import shutil
from pydub import AudioSegment
import yt_dlp as youtube_dl
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC

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

def add_metadata(file_path, metadata):
    try:
        audio = EasyID3(file_path)
        audio['title'] = metadata.get('title', 'Unknown Title')
        audio['artist'] = metadata.get('artist', 'Unknown Artist')
        audio['album'] = metadata.get('album', 'Unknown Album')
        audio.save()
        print(f"Metadata added for {file_path}")
    except Exception as e:
        print(f"Error adding metadata to {file_path}: {e}")

def download_audio():
    if not check_ffmpeg():
        return  # Stop if ffmpeg isn't found

    try:
        # Prompt user for choice
        choice = input("Do you want to download a single track or a playlist? (Enter 'track' or 'playlist'): ").strip().lower()

        if choice not in ['track', 'playlist']:
            print("Invalid choice. Please enter 'track' or 'playlist'.")
            return

        # Prompt for YouTube URL
        url = input("Enter the YouTube URL: ")

        # Set different output templates for track or playlist
        output_template = 'downloaded_audio/%(title)s.%(ext)s' if choice == 'playlist' else 'downloaded_audio.%(ext)s'

        # yt-dlp options
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_template,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'postprocessor_hooks': [embed_metadata_hook],
            'writeinfojson': True,  # Save metadata in JSON files
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading and converting audio...")
            ydl.download([url])

        print("Download and conversion completed!")

    except Exception as e:
        print("An error occurred during the download or conversion process. Please try again.")
        print(f"Error details: {e}")

def embed_metadata_hook(d: dict):
    if d['status'] == 'finished':
        print(f"Processing metadata for {d['info_dict'].get('title', 'Unknown Title')}...")

        # Extract the filename for the downloaded file
        filename = d['info_dict'].get('_filename', '').replace('.webm', '.mp3')
        if not filename:
            print("Filename not found in the downloaded information.")
            return

        json_file = f"{os.path.splitext(filename)[0]}.info.json"
        if os.path.exists(json_file):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    metadata = json.load(f)

                # Extract and add metadata
                metadata_dict = {
                    'title': metadata.get('title', 'Unknown Title'),
                    'artist': metadata.get('artist', 'Unknown Artist'),
                    'album': metadata.get('album', 'Unknown Album'),
                }
                add_metadata(filename, metadata_dict)
            except Exception as e:
                print(f"Error reading metadata from JSON file: {e}")
        else:
            print(f"Metadata file not found for {filename}.")

# Run the function
download_audio()
