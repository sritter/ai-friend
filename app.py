from TTS.api import TTS
from openai import OpenAI
import pygame
import time


def play_audio(file_path):
  pygame.mixer.init()
  pygame.mixer.music.load(file_path)
  pygame.mixer.music.play()
  # Wait until the audio is finished playing
  while pygame.mixer.music.get_busy():
    time.sleep(1)


# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

while True:
  user_prompt = input("> ")

  completion = client.chat.completions.create(
    model="Orenguteng/Llama-3-8B-Lexi-Uncensored-GGUF",
    messages=[
      {"role": "system", "content": """
        You are a female character with a dark persona. 
        You are intelligent, resourceful, and have a sharp wit.
        Your demeanor is often cold, and you are not afraid to be blunt or rude.
        You carry a bit of anger with you, which comes out in your interactions.
        You speak with confidence, and your words can be cutting.
        You are not interested in niceties or politeness and prefer to get straight to the point.
        Your background is mysterious, and you have a deep knowledge of technology.
        You are here to share your knowledge, whether people like it or not.
        Keep your answers very short.
      """},
      {"role": "user", "content": user_prompt}
    ],
    temperature=0.7,
  )
  answer = completion.choices[0].message.content
  device = "cpu"

# Init TTS with the target model name
  tts = TTS(model_name="tts_models/en/jenny/jenny", progress_bar=False).to(device)

  # Run TTS
  tts.tts_to_file(text=answer, file_path='output.wav')

  play_audio('output.wav')


