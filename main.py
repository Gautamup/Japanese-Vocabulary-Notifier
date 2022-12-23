from winotify import Notification, audio
import time
from gtts import gTTS
import pygame

from io import BytesIO
import random
import schedule

def main():
    list=["love あい ",
    "red あか aka",
    "house いえ ie",
    "squid いか ika",
    "train station えき eki",
    "top うえ ue",
    "face かお kao",
    "oyster かき kaki",
    "chrysanthemum きく kiku",
    "carp こい koi",
    "cow うし ushi",
    "lie うそ uso",
    "umbrella かさ kasa",
    "sushi すし sushi",
    "world せかい sekai",
    "octopus たこ tako",
    "subway ちかてつ chikatetsu",
    "moon つき tsuki",
    "home uchi",
    "hand te",
    "eagle taka",
    "basement chika",
    "iron tetsu",
    "dog いぬ inu",
    "fish さかな sakana",
    "sand すな suna",
    "summer なつ natsu",
    "meat にく niku",
    "cat ねこ neko",
    "flower はな hana",
    "fire ひ hi",
    "ship ふね fune",
    "star ほし hoshi",
    "chopsticks hashi",
    "country kuni",
    "pear nashi",
    "hole ana",
    "grave haka",
    "foot/leg あし ashi",
    "head あたま atama",
    "belly おなか onaka",
    "face かお kao",
    "mouth くち kuchi",
    "back せなか senaka",
    "nose はな hana",
    "ear みみ mimi",
    "eye め me",
    "あめ ame rain",
    "いし ishi stone",
    "いわ iwa rock",
    "うみ umi ocean",
    "かわ kawa river",
    "き ki tree",
    "くも kumo cloud",
    "そら sora sky",
    "たに tani valley",
    "つき tsuki the moon",
    "つち tsuchi soil",
    "ひ hi fire",
    "ほし hoshi star",
    "やま yama mountain",
    "ゆき yuki snow",
    "father おとうさん otōsan",
    "mother おかあさん okāsan",
    "older brother おにいさん onīsan",
    "older sister おねえさん onēsan" ,
    "teacher せんせい sensei",
    "ice こおり kōri",
    "street とうり tōri",
    "postage stamp きって kitte"]
    pick= random.choice(list)

    notify= Notification(app_id="python",
                        title="The Word is",
                        msg=pick,duration="short",icon=r"C:\Users\upadh\Desktop\Coding\Python\New japanese word\img.jpg")

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