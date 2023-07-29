# import os
# import torch
# import librosa
# import soundfile as sf

# from pytube import YouTube
# from pydub import AudioSegment
# from huggingsound import SpeechRecognitionModel
# from transformers import pipeline

# # VIDEO_URL = 'https://www.youtube.com/watch?v=h-JVjs9AAmQ' #batman
# #VIDEO_URL = "https://www.youtube.com/watch?v=hWLf6JFbZoo" #obama
# VIDEO_URL = 'https://youtu.be/qNJRGHk7sN8' #english

# yt = YouTube(VIDEO_URL)

# yt.streams \
#   .filter(only_audio = True, file_extension = 'mp4') \
#   .first() \
#   .download(filename = 'ytaudio.mp4') \

# inputdir = r'D:\Summarizer'

# for filename in os.listdir(inputdir):
#     actual_filename = filename[:-4]
#     if(filename.endswith(".mp4")):
#         os.system('ffmpeg -i {} -acodec pcm_s16le -ar 16000 {}.wav'.format(filename, actual_filename))
#     else:
#         continue

# device = "cuda" if torch.cuda.is_available() else "cpu"

# model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-english", device = device)
# input_file = r'D:\Summarizer\ytaudio.wav'

# stream = librosa.stream(
#     input_file,
#     block_length=30,
#     frame_length=16000,
#     hop_length=16000
# )

# for i,speech in enumerate(stream):
#   sf.write(f'{i}.wav', speech, 16000)

# os.makedirs('/content', exist_ok=True)

# for a in range(i+1):
    
#     silence = AudioSegment.silent(duration=1000)
#     silence.export(f'/content/{a}.wav', format="wav")

# audio_path =[]
# for a in range(i+1):
#   audio_path.append(f'/content/{a}.wav')

# transcriptions = model.transcribe(audio_path)
# full_transcript = ' '
# for item in transcriptions:
#   full_transcript += ''.join(item['transcription'])

# summarization = pipeline('summarization')
# summarized_text = summarization(full_transcript)

# print(summarized_text[0]['summary_text'])

# num_iters = int(len(full_transcript)/1000)
# summarized_text = []
# for i in range(0, num_iters + 1):
#   start = 0
#   start = i * 1000
#   end = (i + 1) * 1000
#   out = summarization(full_transcript[start:end], min_length = 5, max_length=20)
#   out = out[0]
#   out = out['summary_text']
#   summarized_text.append(out)

# summarizer.py
import os
import torch
import librosa
import soundfile as sf
from pytube import YouTube
from transformers import pipeline
from huggingsound import SpeechRecognitionModel
import os
import requests
import certifi
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

def download_youtube_audio(url, output_path):
    # Download audio from YouTube video
    yt = YouTube(url)
    yt.streams.filter(only_audio=True, file_extension='mp4').first().download(filename=output_path)

def convert_to_wav(input_dir):
    # Convert downloaded mp4 files to wav format using ffmpeg
    for filename in os.listdir(input_dir):
        actual_filename = filename[:-4]
        if filename.endswith(".mp4"):
            os.system('ffmpeg -i {} -acodec pcm_s16le -ar 16000 {}.wav'.format(filename, actual_filename))
        else:
            continue

def transcribe_audio(model, input_file):
    # Transcribe audio using the HuggingSound SpeechRecognitionModel
    stream = librosa.stream(
        input_file,
        block_length=30,
        frame_length=16000,
        hop_length=16000
    )

    for i, speech in enumerate(stream):
        sf.write(f'{i}.wav', speech, 16000)

    transcriptions = model.transcribe([f'{i}.wav' for i in range(i + 1)])
    full_transcript = ' '.join(item['transcription'] for item in transcriptions)

    return full_transcript

def summarize_text(transcript):
    # Summarize the transcribed text using the HuggingFace pipeline
    summarization = pipeline('summarization')
    num_iters = int(len(transcript) / 1000)
    summarized_text = []
    for i in range(0, num_iters + 1):
        start = i * 1000
        end = (i + 1) * 1000
        out = summarization(transcript[start:end], min_length=5, max_length=20)
        out = out[0]
        out = out['summary_text']
        summarized_text.append(out)

    return summarized_text

def summarize_video(video_url):
    # Specify input and output paths
    input_dir = r'/Users/syedmasroor/Desktop/ytdvidsum'
    input_file = r'/Users/syedmasroor/Desktop/ytdvidsum/ytaudio.wav'

    # Download and convert audio
    download_youtube_audio(video_url, 'ytaudio.mp4')
    convert_to_wav(input_dir)

    # Initialize the speech recognition model
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-english", device=device)

    # Transcribe and summarize the video's audio
    full_transcript = transcribe_audio(model, input_file)
    summarized_text = summarize_text(full_transcript)

    return summarized_text

