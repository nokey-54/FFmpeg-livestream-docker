import os
import random
import tempfile
import subprocess
import sys

API_KEY = os.environ.get("API_KEY")
FOLDER = os.environ.get("FOLDER", "mp3") # replace ls01.png in stream01 folder to replace background
IMAGE = os.environ.get("IMAGE", "./ls01.png") # replace ls01.png in stream01 folder to replace background

print(API_KEY, FOLDER, IMAGE)

system_dir = os.path.dirname(os.path.realpath(__file__))
mp3_dir = os.path.join(system_dir, FOLDER)

if os.path.isdir(mp3_dir):
    print(f"The '{FOLDER}' directory exists within the '{system_dir}' directory.")
else:
    print(f"The '{FOLDER}' directory does not exist within the '{system_dir}' directory.")
    
if not API_KEY or API_KEY == "":
    print("API_KEY not set, please set the environment variable with your API key.")
    sys.exit(1)

mp3_files = [f for f in os.listdir(FOLDER) if f.endswith('.mp3')]

if not mp3_files:
    print(f"No MP3 files found in the specified folder: {FOLDER}")
    sys.exit(1)

while True:
    random.shuffle(mp3_files)

    # Create a temporary file to store the mp3 playlist
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_playlist_file:
        temp_playlist_file.writelines([f"file '{os.path.abspath(os.path.join(FOLDER, mp3_file))}'\n" for mp3_file in mp3_files])
        temp_playlist_file_name = temp_playlist_file.name

    ffmpeg_cmd = [
        "ffmpeg", "-loglevel", "info", "-y", "-re",
        "-f", "image2", "-loop", "1", "-i", IMAGE,
        "-f", "concat", "-safe", "0", "-protocol_whitelist", "file", "-i", temp_playlist_file_name,
        "-c:v", "libx264", "-preset", "veryfast", "-b:v", "2000k", "-maxrate", "2000k", "-bufsize", "4000k",
        "-framerate", "25", "-video_size", "1280x720", "-vf", "format=yuv420p", "-g", "50", "-shortest", "-strict", "experimental",
        "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
        "-f", "flv", f"rtmp://a.rtmp.youtube.com/live2/{API_KEY}"
    ]

    # Start the ffmpeg process
    ffmpeg_process = subprocess.Popen(ffmpeg_cmd)

    # Wait for the ffmpeg process to finish
    ffmpeg_process.wait()

    # Delete the temporary playlist file
    os.unlink(temp_playlist_file_name)

    # Restart the script if the ffmpeg process exits with a non-zero code
    if ffmpeg_process.returncode != 0:
        print(f"ffmpeg exited with code {ffmpeg_process.returncode}, restarting...")
        continue
