import proto
from google.cloud import speech
import io


def transcribe_file(speech_file): #todo вернуть текст строкой! string
    client = speech.SpeechClient()

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig()
    config.encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16
    config.sample_rate_hertz = 16000
    config.language_code = "en-US"

    response = client.recognize(config=config, audio=audio)
    transcription = ""
    for result in response.results:
        transcription += result.alternatives[0].transcript
        print("Transcript: {}".format(result.alternatives[0].transcript))
    return transcription