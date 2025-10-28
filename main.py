from winotify import Notification, audio
import time
from gtts import gTTS
from io import BytesIO
import random
import schedule
import ast
import pygame
from dotenv import load_dotenv
from google import genai
from google.genai import types
import os
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client()

def main():
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction="""You are a Japanese vocabulary generator. 
                Your task is to output useful Japanese words for learners. 
                Each entry must include one English word followed by its Japanese translation in Hiragana or Katakana, separated by a space.
                Do not include Romaji or explanations.

                Format strictly like this:
                love あい
                red あか
                cat ねこ

                Generate 10 new random words each time.
                The words must be in a python list
                """,
            thinking_config=types.ThinkingConfig(thinking_budget=0)
        ),
        contents="Generate a new list of Japanese words.",
        
    )
    llm_output = response.text
    # Extract and safely evaluate the Python list
    start = llm_output.find('[')
    end = llm_output.rfind(']') + 1
    list_str = llm_output[start:end]

    words = ast.literal_eval(list_str)

    pick= random.choice(words)

    notify= Notification(app_id="python",
                        title="The Word is",
                        msg=pick,duration="short",icon=r"C:\Users\upadh\Desktop\Coding\Japanese-Vocabulary-Notifier\img.jpg")

    notify.show()
    def speak(text):
        temp_file=BytesIO()
        tts = gTTS( text, lang='ja')
        tts.write_to_fp(temp_file)
        return temp_file
    pygame.init()
    pygame.mixer.init()
    sound = speak(pick)
    sound.seek(0)
    pygame.mixer.music.load(sound, "mp3")
    pygame.mixer.music.play()

schedule.every(30).seconds.do(main)
while True:
    schedule.run_pending()
    time.sleep(1)