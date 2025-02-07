# YouTube Transcriber

This project is a Python application that transcribes audio from YouTube videos into text files. It allows users to input a YouTube video URL, downloads the audio, and converts it into a text format.

## Project Structure

```
youtube-transcriber   (Windows OS)
├── tools
│   ├── vosk-model      # Speech recognition toolkit 
│   ├── ffmpeg.exe      # FFmpeg executable for audio processing
│   ├── ffprobe.exe     # FFprobe executable for audio processing
├── src
│   ├── main.py          # Entry point of the application
│   ├── transcriber.py   # Contains the Transcriber class for audio processing
│   └── utils
│       └── __init__.py  # Utility functions for the project
├── requirements.txt      # Lists project dependencies
└── README.md             # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd youtube-transcriber
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create the tools folder at the root level.

4. Create the vosk-model folder inside the tools folder and add the files of the downloaded model according to the language.
(https://alphacephei.com/vosk/models) Link download.

      youtube-transcriber
      ├── tools
      │   ├── vosk-model (Here)

5. Download the audio processor ffmpeg and ffprobe according to your OS and unzip it in the tools folder. If your OS is Windows you should place the two .exe executables in the tools folder.
(https://ffmpeg.org/download.html) link donload.

## Usage

1. Run the application:
   ```
   python src/main.py <YouTube Video URL>
   ```

2. The transcription will be saved to a text file in the project directory.

## Dependencies

- `vosk`: Speech recognition toolkit.
- `soundfile`: Library for reading and writing sound files.
- `youtube_dl`: Download videos from youtube.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.
