from pyrogram import Client
from pyrogram import filters
import asyncio
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
from requests import get
import os
import openai
from gtts import gTTS

api_id = 22805944
api_hash = "95c8e4b7397e7c755fe022231a95b667"
bot_token = "5853610677:AAHhgfEGrOgXNQqBelQip4Iev6sp8Zfpyag"
openai.api_key = "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"
model_engine = "text-davinci-003"

app = Client(
    "lambdasession",
    api_id=api_id, api_hash=api_hash, bot_token=bot_token
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await client.send_message(message.chat.id, f"""Hey, I'm alive! You don't need to send a command to me. Let's talk with me right now!
""", reply_markup=InlineKeyboardMarkup(
			[
            	[
                InlineKeyboardButton(
                "Owner",
                url="https://t.me/LambdaSanctuary"
                )],
                [
                InlineKeyboardButton("ChatGPT", url="https://chat.openai.com")
                ]
			]))

@app.on_message(filters.text)
async def c(client, message):
	prompt = message.text
	# Generate a response
	completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5)
	response = completion.choices[0].text
	await client.send_message(message.chat.id, response)

app.run()
