import pyttsx3
import requests
from pydub import AudioSegment
from pydub.playback import play
import argparse

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

def main():
    parser = argparse.ArgumentParser(description='Local Bot Command Line Interface')
    subparsers = parser.add_subparsers(dest='command')

    # Misc commands
    parser_a = subparsers.add_parser('a')
    parser_a.add_argument('alias_name')
    parser_a.add_argument('--create', action='store_true')
    parser_a.add_argument('--delete', action='store_true')

    parser_bot = subparsers.add_parser('bot')
    parser_bot.add_argument('action', choices=['on', 'off', 'info'])

    parser_gnagnagna = subparsers.add_parser('gnagnagna')
    parser_gnagnagna.add_argument('user', nargs='?')

    subparsers.add_parser('help')

    parser_lunch = subparsers.add_parser('lunch')
    parser_lunch.add_argument('date')

    subparsers.add_parser('quote')
    subparsers.add_parser('repeat')
    subparsers.add_parser('weather')

    # Audio commands
    parser_audio = subparsers.add_parser('audio')
    parser_audio.add_argument('action', choices=['get', 'set'])
    parser_audio.add_argument('idx', type=int, nargs='?')

    parser_play = subparsers.add_parser('play')
    parser_play.add_argument('url')

    parser_rec = subparsers.add_parser('rec')
    parser_rec.add_argument('name')
    parser_rec.add_argument('--delete', action='store_true')

    subparsers.add_parser('stop')

    parser_vol = subparsers.add_parser('vol')
    parser_vol.add_argument('volume', type=int)

    # Reddit commands
    subparsers.add_parser('aww')
    subparsers.add_parser('gif')
    subparsers.add_parser('joke')

    parser_redgif = subparsers.add_parser('redgif')
    parser_redgif.add_argument('subreddit')

    parser_redpic = subparsers.add_parser('redpic')
    parser_redpic.add_argument('subreddit')

    parser_redplay = subparsers.add_parser('redplay')
    parser_redplay.add_argument('subreddit')

    parser_redpost = subparsers.add_parser('redpost')
    parser_redpost.add_argument('subreddit')

    # Common options
    parser_lang = subparsers.add_parser('lang')
    parser_lang.add_argument('language')

    args = parser.parse_args()

    if args.command == 'a':
        if args.create:
            create_alias(args.alias_name)
        elif args.delete:
            delete_alias(args.alias_name)
        else:
            run_alias(args.alias_name)
    elif args.command == 'bot':
        bot_info(args.action)
    elif args.command == 'gnagnagna':
        gnagnagna(args.user)
    elif args.command == 'help':
        display_help()
    elif args.command == 'lunch':
        lunch(args.date)
    elif args.command == 'quote':
        quote()
    elif args.command == 'repeat':
        repeat('last command')
    elif args.command == 'weather':
        weather()
    elif args.command == 'audio':
        if args.action == 'get':
            get_audio_info(args.idx)
        elif args.action == 'set':
            set_audio_output(args.idx)
    elif args.command == 'play':
        play_audio(args.url)
    elif args.command == 'rec':
        if args.delete:
            delete_recording(args.name)
        else:
            record_audio(args.name)
    elif args.command == 'stop':
        stop_player()
    elif args.command == 'vol':
        change_volume(args.volume)
    elif args.command == 'aww':
        reddit_picture('aww')
    elif args.command == 'gif':
        reddit_gif('gif')
    elif args.command == 'joke':
        reddit_joke()
    elif args.command == 'redgif':
        reddit_gif(args.subreddit)
    elif args.command == 'redpic':
        reddit_picture(args.subreddit)
    elif args.command == 'redplay':
        reddit_audio(args.subreddit)
    elif args.command == 'redpost':
        reddit_post(args.subreddit)
    elif args.command == 'lang':
        change_language(args.language)

if __name__ == '__main__':
    main()
