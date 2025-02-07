import subprocess

class Transcriber:
    def __init__(self, video_url):
        self.video_url = video_url
        self.audio_file = None
        self.transcription = None

    def fetch_video_audio(self):
        import yt_dlp as youtube_dl
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': 'audio.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'wav',
                    'preferredquality': '192',
                }],
                'ffmpeg_location': '..\\tools\\ffmpeg.exe', 
                'ffprobe_location': '..\\tools\\ffprobe.exe'
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.video_url])
            self.audio_file = 'audio.wav'
            self.convert_to_mono_pcm()
        except Exception as e:
            print(f"An error occurred while fetching video audio: {e}")
            raise

    def convert_to_mono_pcm(self):
        try:
            subprocess.run([
                '..\\tools\\ffmpeg.exe', '-i', self.audio_file, '-ac', '1', '-ar', '16000', '-y', 'audio_mono.wav'
            ], check=True)
            self.audio_file = 'audio_mono.wav'
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while converting audio: {e}")
            raise

    def transcribe_audio(self):
        from vosk import Model, KaldiRecognizer
        import wave
        import json

        model = Model("..\\tools\\vosk-model") # Specify the path to the Vosk model
        wf = wave.open(self.audio_file, "rb")
        if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
            raise ValueError("Audio file must be WAV format mono PCM.")

        rec = KaldiRecognizer(model, wf.getframerate())
        self.transcription = ""

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                self.transcription += result.get("text", "") + " "

        result = json.loads(rec.FinalResult())
        self.transcription += result.get("text", "")

    def save_transcription(self, filename='transcription.txt'):
        if self.transcription:
            with open(filename, 'w') as f:
                f.write(self.transcription)
        else:
            print("No transcription available to save.")