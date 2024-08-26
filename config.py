from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("26173917")
APP_HASH = os.environ.get("d566bf611b29ecff0a3b91986637b957")
BOT_USERNAME = os.environ.get("ghazllpbot")
session = os.environ.get("BAGPYd0An_OkU1Zti-2oSzVsh54Z1nWNI8MsQ4Dm0nkvBzQByQ35PRj2Pcmq6IRns7P_ps5GghNHG6wfOrPwXRV_yQXk8pLvUpCGczGuDa7Vpv6ZcUEz2DPRmgtr5bbF398NAYRVe7DOAwO-_sZC0yWDpaMh_D1lyUXxv9liDNXZEWCvqBlsbLg1Af2eUjYMjG3w0nm8K5hAQcfqPbaN8I33xw99HKUbbbl26Dg3Vrm3Htxg6zhL_AaTdfsOdC_T8IhwquHAlaNL6Gl0ZG9NUrprViVqo5cd0mWOHn0_uHjdk_52KwNpcix3alEOPSKDFwiz7rDnwJPwzhP6hqIaw0plwm0IKwAAAAFimA2JAA")
SESSION = os.environ.get("BAGPYd0An_OkU1Zti-2oSzVsh54Z1nWNI8MsQ4Dm0nkvBzQByQ35PRj2Pcmq6IRns7P_ps5GghNHG6wfOrPwXRV_yQXk8pLvUpCGczGuDa7Vpv6ZcUEz2DPRmgtr5bbF398NAYRVe7DOAwO-_sZC0yWDpaMh_D1lyUXxv9liDNXZEWCvqBlsbLg1Af2eUjYMjG3w0nm8K5hAQcfqPbaN8I33xw99HKUbbbl26Dg3Vrm3Htxg6zhL_AaTdfsOdC_T8IhwquHAlaNL6Gl0ZG9NUrprViVqo5cd0mWOHn0_uHjdk_52KwNpcix3alEOPSKDFwiz7rDnwJPwzhP6hqIaw0plwm0IKwAAAAFimA2JAA")
token = os.environ.get("7495525018:AAFSBMAJ03H1MHsRSiw3meeMv25LECG-Btc")
ze = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()