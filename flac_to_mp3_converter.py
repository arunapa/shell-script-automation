import os
import shutil
import subprocess
import time

MUSIC_LIBRARY_PATH = "/Users/aruna/Music"

if __name__ == "__main__":
    # Check if ffmpeg is installed
    ffmpeg_path = shutil.which("ffmpeg")
    if ffmpeg_path is None:
        print("ffmpeg not installed! aborting...")
        exit(1)

    total = 0
    converted = 0

    print("scanning for .flac files...")

    # Iterate over .flac files
    for root, dirs, files in os.walk(MUSIC_LIBRARY_PATH):
        for file in files:
            if file.endswith(".flac"):
                total += 1
                flac_file = os.path.join(root, file)
                mp3_file_name = flac_file.replace(".flac", ".mp3")
                
                # Convert flac to mp3 using ffmpeg
                try:
                    subprocess.run([
                        "ffmpeg", "-y", "-i", flac_file, "-ab", "320k", "-map_metadata", "0", "-id3v2_version", "3", mp3_file_name
                    ], check=True)
                    converted += 1
                
                except subprocess.CalledProcessError:
                    print(f"Couldn't convert {flac_file} :(")
                    time.sleep(15)

    print(f"done converting {converted} files, {total} files found in total")

    
