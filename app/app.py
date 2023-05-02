import config
from STT import stt
from NickVoice import bot_voice
from fuzzywuzzy import fuzz
import random


def va_respond(voice: str):
    print(voice)
    if voice.startswith(config.BOT_ALTER_NAMES):

        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in config.BOT_COMMANDS.keys():
            bot_voice.bot_speak("Что?")
        else:
            execute_cmd(cmd['cmd'])


def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.BOT_ALTER_NAMES:
        cmd = cmd.replace(x, "").strip()

    for x in config.BOT_PHRASES:
        cmd = cmd.replace(x, "").strip()

    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.BOT_COMMANDS.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc


def execute_cmd(cmd: str):
    if cmd == 'help':
        # help
        text = "Я умею: ..."
        text += "произносить время ..."
        text += "рассказывать анекдоты ..."
        text += "в будущем никита добавит еще функционал"

        bot_voice.bot_speak(text)
        pass

    elif cmd == 'joke':
        jokes = config.BOT_JOKES
        bot_voice.bot_speak(random.choice(jokes))


# начать прослушивание команд
stt.bot_listen(va_respond)
