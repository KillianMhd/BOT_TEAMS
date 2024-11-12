import pyttsx3
import requests
from pydub import AudioSegment
from pydub.playback import play

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def create_alias(alias_name):
    speak(f'Alias {alias_name} created.')

def delete_alias(alias_name):
    speak(f'Alias {alias_name} deleted.')

def run_alias(alias_name):
    speak(f'Running alias {alias_name}.')

def bot_info(action):
    if action == 'on':
        speak('Bot is now ON.')
    elif action == 'off':
        speak('Bot is now OFF.')
    elif action == 'info':
        speak('Bot info: [Your bot info here]')

def gnagnagna(user=None):
    if user:
        speak(f'gnagnagna {user}')
    else:
        speak('gnagnagna mode off.')

def display_help():
    speak('Help: [Your help message here]')

def lunch(date):
    speak(f'Nearby lunch options for {date}: [Your lunch options here]')

def quote():
    response = requests.get('https://zenquotes.io/api/random')
    if response.status_code == 200:
        quote = response.json()[0]['q']
        speak(quote)
    else:
        speak('Could not retrieve quote.')

def repeat(last_command):
    speak(f'Repeating last command: {last_command}')

def weather():
    speak('Current weather: [Your weather info here]')

def get_audio_info(idx):
    speak(f'Getting audio info for IDX {idx}.')

def set_audio_output(idx):
    speak(f'Setting audio output to IDX {idx}.')

def play_audio(url):
    audio = AudioSegment.from_file(url)
    play(audio)

def record_audio(name):
    speak(f'Recording audio sample {name}.')

def delete_recording(name):
    speak(f'Recording {name} deleted.')

def stop_player():
    speak('Stopping player.')

def change_volume(volume):
    engine.setProperty('volume', volume / 100)
    speak(f'Changing volume to {volume}.')

def reddit_picture(subreddit):
    speak(f'Picture from r/{subreddit}.')

def reddit_gif(subreddit):
    speak(f'Gif from r/{subreddit}.')

def reddit_joke():
    speak('Joke from r/dadjokes.')

def reddit_audio(subreddit):
    speak(f'Playing audio from r/{subreddit}.')

def reddit_post(subreddit):
    speak(f'Post from r/{subreddit}.')

def change_language(language):
    speak(f'Changing language to {language}.')

