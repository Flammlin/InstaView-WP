# pip3 install beautifulsoup4
# pip install pytelegrambotapi
import argparse
import os
from argparse import ArgumentParser
import telebot
from urllib.request import urlopen
from bs4 import BeautifulSoup

bot = telebot.TeleBot('TokenBot')
idusers = 'chat-id'

parser: ArgumentParser = argparse.ArgumentParser(description='Send message')
parser.add_argument('-m', default=os.environ.get('URL'), action="store", dest="Url", required=True)
args = parser.parse_args()

UrlF = "https://t.me/iv?url="
UrlL = "&rhash=04e540677155a7"
UrlTG = UrlF + args.Url + UrlL

soup = BeautifulSoup(urlopen(args.Url), "html.parser")
Title = soup.title.get_text()
Header = Title.rstrip(' - Всяко разно') # Delete  - Всяко разно

text = "[" + Header + "]" + "(" + UrlTG + ")" + '\n' + args.Url

bot.send_message(idusers, text, parse_mode= 'Markdown')