from openai import OpenAI
from functions import remove_punctuation,whitespace_indexes,sentiments

API_KEY="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"
audio_path = "../records/records.wav"

client = OpenAI(api_key=API_KEY)
audio_file = open(audio_path, "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file,
  language="tr"
)

text = remove_punctuation(transcript.text)
print(text)
print(len(text))

index_of_whitespaces = whitespace_indexes(text)

print(len(index_of_whitespaces))

sentiments = sentiments(text, index_of_whitespaces)

print(sentiments)

