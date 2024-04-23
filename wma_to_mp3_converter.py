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

    print("scanning for .wma files...")

    # Iterate over .wma files
    for root, dirs, files in os.walk(MUSIC_LIBRARY_PATH):
        for file in files:
            if file.endswith(".wma"):
                total += 1
                wma_file = os.path.join(root, file)
                mp3_file_name = wma_file.replace(".wma", ".mp3")
                
                # Convert wma to mp3 using ffmpeg
                try:
                    subprocess.run([
                        "ffmpeg", "-y", "-i", wma_file, "-ab", "320k", "-map_metadata", "0", "-id3v2_version", "3", mp3_file_name
                    ], check=True)
                    converted += 1
                
                except subprocess.CalledProcessError:
                    print(f"Couldn't convert {wma_file} :(")
                    time.sleep(15)

    print(f"done converting {converted} files, {total} files found in total")
