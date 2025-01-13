import os
import shutil
import json
from pydub import AudioSegment
import yt_dlp as youtube_dl
from mutagen.easyid3 import EasyID3

def check_ffmpeg():
    ffmpeg_path = shutil.which("ffmpeg")
    if not ffmpeg_path:
        print("FFmpeg is not installed or not found in PATH. Please install it and ensure it is in your system's PATH.")
        return False
    print(f"FFmpeg found at: {ffmpeg_path}")
    return True

def add_metadata(file_path, metadata):
    try:
        audio = EasyID3(file_path)
        audio.update(metadata)
        audio.save()
        print(f"Metadata added for {file_path}")
    except Exception as e:
        print(f"Error adding metadata: {e}")

def download_audio():
    if not check_ffmpeg():
        return

    url = input("Enter the YouTube URL: ")
    if not any(x in url for x in ["youtube.com", "youtu.be"]):
        print("Invalid URL. Please enter a correct YouTube URL.")
        return

    # Check if the URL is a playlist
    is_playlist = 'list=' in url
    output_template = 'downloaded_audio/%(playlist_title)s/%(title)s.%(ext)s' if is_playlist else 'downloaded_audio/%(title)s.%(ext)s'

    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': output_template,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': not is_playlist,
        'writeinfojson': True,
        'quiet': False,
        'postprocessor_hooks': [embed_metadata_hook]
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading and converting audio...")
        result = ydl.download([url])
        print("Download and conversion completed!" if result == 0 else "Download failed.")

def embed_metadata_hook(d):
    if d['status'] == 'finished':
        # Safely retrieve the filename with a default fallback
        filename = d.get('filename')
        if not filename:
            print("Error: No filename found in download data.")
            return
        
        print(f"Finished downloading {filename}, processing metadata...")
        try:
            # Ensure filename has the correct extension
            filename = filename.replace('.webm', '.mp3')
            json_file = os.path.splitext(filename)[0] + '.info.json'
            
            if os.path.exists(json_file):
                with open(json_file, 'r', encoding='utf-8') as f:
                    metadata = json.load(f)
                add_metadata(filename, {
                    'title': metadata.get('title', 'Unknown Title'),
                    'artist': metadata.get('uploader', 'Unknown Artist'),
                    'album': 'YouTube Download'
                })
            else:
                print("Metadata file not found.")
        except Exception as e:
            print(f"Error processing metadata: {e}")

# Run the function
download_audio()
