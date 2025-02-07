def main():
    import sys
    from transcriber import Transcriber

    if len(sys.argv) != 2:
        print("Usage: python main.py <YouTube Video URL>")
        return

    video_url = sys.argv[1]
    transcriber = Transcriber(video_url)

    try:
        transcriber.fetch_video_audio()
        transcriber.transcribe_audio()
        transcriber.save_transcription()
        print("Transcription completed and saved to transcription.txt")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()