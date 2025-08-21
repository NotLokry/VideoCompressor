# Video Compressor

A simple desktop application to compress MP4 video files to approximately 10 MB using a graphical interface built with CustomTkinter and MoviePy.

## Features

- Select and compress MP4 files
- Output video is scaled to 720p and saved as `output.mp4`
- Estimated target size: ~10 MB
- Audio bitrate set to 128 kbps

## Usage

1. Run `main.py`.
2. Click **Open a File** and select an MP4 video.
3. The app will compress the video and save it as `output.mp4` in the current directory.
4. A message will confirm when compression is complete.

## Requirements

- Python 3.x
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [MoviePy](https://zulko.github.io/moviepy/)
- [TempFile](https://docs.python.org/3/library/tempfile.html)

Install dependencies with:

```sh
pip install customtkinter moviepy