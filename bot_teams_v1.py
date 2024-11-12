import asyncio
from aiohttp import web
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity, ActivityTypes

class TeamsBot:
    async def on_turn(self, turn_context: TurnContext):
        if turn_context.activity.type == ActivityTypes.message:
            text = turn_context.activity.text.lower()
            if text.startswith('!a'):
                await self.handle_a_command(turn_context, text)
            elif text.startswith('!bot'):
                await self.handle_bot_command(turn_context, text)
            elif text.startswith('!gnagnagna'):
                await self.handle_gnagnagna_command(turn_context, text)
            elif text.startswith('!help'):
                await self.handle_help_command(turn_context)
            elif text.startswith('!lunch'):
                await self.handle_lunch_command(turn_context, text)
            elif text.startswith('!quote'):
                await self.handle_quote_command(turn_context)
            elif text.startswith('!repeat'):
                await self.handle_repeat_command(turn_context)
            elif text.startswith('!weather'):
                await self.handle_weather_command(turn_context)
            elif text.startswith('!audio'):
                await self.handle_audio_command(turn_context, text)
            elif text.startswith('!play'):
                await self.handle_play_command(turn_context, text)
            elif text.startswith('!rec'):
                await self.handle_rec_command(turn_context, text)
            elif text.startswith('!speak'):
                await self.handle_speak_command(turn_context, text)
            elif text.startswith('!stop'):
                await self.handle_stop_command(turn_context)
            elif text.startswith('!vol'):
                await self.handle_vol_command(turn_context, text)
            elif text.startswith('!aww'):
                await self.handle_aww_command(turn_context)
            elif text.startswith('!gif'):
                await self.handle_gif_command(turn_context)
            elif text.startswith('!joke'):
                await self.handle_joke_command(turn_context)
            elif text.startswith('!redgif'):
                await self.handle_redgif_command(turn_context, text)
            elif text.startswith('!redpic'):
                await self.handle_redpic_command(turn_context, text)
            elif text.startswith('!redplay'):
                await self.handle_redplay_command(turn_context, text)
            elif text.startswith('!redpost'):
                await self.handle_redpost_command(turn_context, text)
            elif '--lang' in text:
                await self.handle_lang_command(turn_context, text)
            elif '--speak' in text:
                await self.handle_speak_option(turn_context, text)

    async def handle_a_command(self, turn_context, text):
        # Handle !a command
        await turn_context.send_activity(f'Alias command received: {text}')

    async def handle_bot_command(self, turn_context, text):
        # Handle !bot command
        await turn_context.send_activity(f'Bot command received: {text}')

    async def handle_gnagnagna_command(self, turn_context, text):
        # Handle !gnagnagna command
        await turn_context.send_activity(f'gnagnagna command received: {text}')

    async def handle_help_command(self, turn_context):
        help_message = """
        !a [ALIAS_NAME] [--create|--delete] : create/run aliases
        !bot on|off|info : robot info and actions
        !gnagnagna @**SOMEONE**|off : reply 'gnagnagna' everytime someone talks
        !help : display this help
        !lunch [dd/mm] : display nearby lunch options for a specific day
        !quote : Random zen quote from zenquotes.io
        !repeat : repeat last command
        !weather : print current weather
        !audio get|set IDX : get audio info, set output
        !play [URL] : play audio from url or recorded samples
        !rec [NAME] [--delete] : record audio samples of 5 sec
        !speak TEXT : speak in french
        !stop : stop player
        !vol INT : change volume
        !aww : picture from reddit r/aww
        !gif : gif from reddit r/gif
        !joke : joke from reddit r/dadjokes
        !redgif [SUBREDDIT] : gif from reddit
        !redpic [SUBREDDIT] : picture from reddit
        !redplay [SUBREDDIT] : play audio from reddit
        !redpost [SUBREDDIT] : post from reddit
        --lang : change spoken language of the cmd
        --speak : say the msg instead of printing it
        """
        await turn_context.send_activity(help_message)

    async def handle_lunch_command(self, turn_context, text):
        # Handle !lunch command
        await turn_context.send_activity(f'Lunch options: {text}')

    async def handle_quote_command(self, turn_context):
        # Handle !quote command
        await turn_context.send_activity('Random zen quote: [Your quote here]')

    async def handle_repeat_command(self, turn_context):
        # Handle !repeat command
        await turn_context.send_activity('Repeating last command.')

    async def handle_weather_command(self, turn_context):
        # Handle !weather command
        await turn_context.send_activity('Current weather: [Your weather info here]')

    async def handle_audio_command(self, turn_context, text):
        # Handle !audio command
        await turn_context.send_activity(f'Audio command received: {text}')

    async def handle_play_command(self, turn_context, text):
        # Handle !play command
        await turn_context.send_activity(f'Playing audio from {text}')

    async def handle_rec_command(self, turn_context, text):
        # Handle !rec command
        await turn_context.send_activity(f'Recording audio sample: {text}')

    async def handle_speak_command(self, turn_context, text):
        # Handle !speak command
        await turn_context.send_activity(f'Speaking in French: {text}')

    async def handle_stop_command(self, turn_context):
        # Handle !stop command
        await turn_context.send_activity('Stopping player.')

    async def handle_vol_command(self, turn_context, text):
        # Handle !vol command
        await turn_context.send_activity(f'Volume set to {text}')

    async def handle_aww_command(self, turn_context):
        # Handle !aww command
        await turn_context.send_activity('Picture from r/aww: [Your picture here]')

    async def handle_gif_command(self, turn_context):
        # Handle !gif command
        await turn_context.send_activity('GIF from r/gif: [Your GIF here]')

    async def handle_joke_command(self, turn_context):
        # Handle !joke command
        await turn_context.send_activity('Joke from r/dadjokes: [Your joke here]')

    async def handle_redgif_command(self, turn_context, text):
        # Handle !redgif command
        await turn_context.send_activity(f'GIF from r/{text}: [Your GIF here]')

    async def handle_redpic_command(self, turn_context, text):
        # Handle !redpic command
        await turn_context.send_activity(f'Picture from r/{text}: [Your picture here]')

    async def handle_redplay_command(self, turn_context, text):
        # Handle !redplay command
        await turn_context.send_activity(f'Playing audio from r/{text}: [Your audio here]')

    async def handle_redpost_command(self, turn_context, text):
        # Handle !redpost command
        await turn_context.send_activity(f'Post from r/{text}: [Your post here]')

    async def handle_lang_command(self, turn_context, text):
        # Handle --lang option
        await turn_context.send_activity(f'Changing language: {text}')

    async def handle_speak_option(self, turn_context, text):
        # Handle --speak option
        await turn_context.send_activity(f'Speaking message: {text}')

async def messages(req):
    body = await req.json()
    activity = Activity().deserialize(body)
    auth_header = req.headers['Authorization'] if 'Authorization' in req.headers else ''
    await ADAPTER.process_activity(activity, auth_header, BOT.on_turn)
    return web.Response(status=201)

APP_ID = 'YOUR_APP_ID'
APP_PASSWORD = 'YOUR_APP_PASSWORD'
SETTINGS = BotFrameworkAdapterSettings(APP_ID, APP_PASSWORD)
ADAPTER = BotFrameworkAdapter(SETTINGS)
BOT = TeamsBot()

app = web.Application()
app.router.add_post('/api/messages', messages)

if __name__ == '__main__':
    web.run_app(app, host='localhost', port=3978)
