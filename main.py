#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from __future__ import unicode_literals
from twx.botapi import TelegramBot
from twx.botapi import InputFile
from twx.botapi import InputFileInfo

import traceback
import feedparser
import random
import http.client

class DigestBot(object):
    token = '5325183488:AAFMiD29IxXGt3Jf1QxEc9TmyLMtQ5GqzcQ' #Super secret bot token
    stack_list = []
    admin = 'Pablozzz'                                      #admin name
 
    def __init__(self):
        self.bot = TelegramBot(self.token)
        self.bot.get_me()
        last_updates = self.bot.get_updates(offset=0).wait()
        try:
            self.last_update_id = list(last_updates)[-1].update_id
        except IndexError:
            self.last_update_id = None
        print('last update id: {0}'.format(self.last_update_id))
 
    def process_message(self, message):                     #function for chech messages and send answers
        text = message.message.text
        chat = message.message.chat
        text = text.strip()
        bot_name = "zaurtox_bot"
                                                            #Substrings in messages = commands
        Toxa = "/Toxa"
        Zaur = "/Zaur"
        News = "/News"
        Help = "/Help"
        Valuta = "/Valuta"
        Start = "/Start"
        Slogan = "/Pogovorka"
        Leha = "/Leha"
        Igor = "/Igor"
        Pasha = "/Pasha"
        Photo = "/Photo"
        Sticker = "/Sticker"
        Bash = "/Bash"
                                                        #logger : print susbstr if catch that in message
        print('Got message: \33[0;32m{0}\33[0m from chat: {1}'.format(text, chat))


        try:
                                                            # commands
            #Help : print all supported commands
            if Help  in text:
                bot_answer = 'Команды /Help /News /Zaur /Toxa /Valuta /Pogovorka /Photo /Sticker /Bash\n'
                try:
                    self.bot.send_message(chat.id, bot_answer)
                except Exception:
                    self.bot.send_message(chat.id, 'Unknow error. Sorry.')
            #Start command it's nessesary for telegramm rules complete
            if Start  in text:
                bot_answer = 'Это эмоциональный бот, который может помочь с новостями и комментариями к ним /Help  \n'
                try:
                    self.bot.send_message(chat.id, bot_answer)
                except Exception:
                    self.bot.send_message(chat.id, 'Unknow error. Sorry.')
            #News parse news from rbc.ru rss and send in chat
            if News in text:
                d = feedparser.parse('http://static.feed.rbc.ru/rbc/internal/rss.rbc.ru/rbc.ru/news.rss')
                bot_answer =d['entries'][0]['title']+" "+d.entries[0]['link']
                try:
                    self.bot.send_message(chat.id, bot_answer)
                except Exception:
                    self.bot.send_message(chat.id, 'Unknow error. Sorry.')
            #Parse currenty rate and send in chat
            if Valuta in text:
                speaker=["Как заявил Антон Силуанов",
                         "Как заявил Алексей Улюкаев",
                         "Как заявила Эльвира Набиулина"]
                i = random.randrange(0,3,1)
                sentense = speaker[i] +", обоснованным курсом рубля явлеется: "
                HOST = "www.sberometer.ru"
                PORT = 80
                conn = http.client.HTTPConnection(HOST, PORT)
                conn.request("GET", "/")
                res = conn.getresponse()
                data = res.read()
                conn.close()
                answer = str(data)
                pos = answer.find("cursNow")
                bot_answer= sentense + answer[(pos+11):(pos+34):1]
                try:
                    self.bot.send_message(chat.id, bot_answer)
                except Exception:
                    self.bot.send_message(chat.id, 'Unknow error. Sorry.')
            #Parse strory from bach.org rss and print in chat
            if Bash in text:
                d = feedparser.parse('http://bash.im/rss/')
                bot_answer =d['entries'][0]['title']+" "+d.entries[0]['link']
                try:
                    self.bot.send_message(chat.id, bot_answer)
                except Exception:
                    self.bot.send_message(chat.id, 'Unknow error. Sorry.')
            #Select random slogan from file "pogovorki.txt" and send in chat
            if Slogan in text:
                fp = open("pogovorki.txt")
                lines = fp.readlines()
                fp.close()
                phrase = ["Как говорил мой дед: ",
                          "Как говорят у нас в народе: ",
                          "Народная мудрость: ",
                          "Как мы все знаем: "]
                a = random.randrange(0,4,1)
                i = random.randrange(0,1353,1)
                slogan = (lines[i].strip())
                bot_answer = phrase[a] + slogan
                try:
                    self.bot.send_message(chat.id, bot_answer)
                except Exception:
                    self.bot.send_message(chat.id, 'Unknow error. Sorry.')
            #Send strickers in chat
            if (text == Sticker):
                stikers = ["BQADAgADeAcAAlOx9wOjY2jpAAHq9DUC"]
                try:
                    self.bot.send_sticker(chat.id, stikers[0])
                except Exception:
                    self.bot.send_photo(chat.id, 'Unknow error. Sorry.')
            #Send photo from /photo path
            if (text == Photo):
                photos = ["photo/photo1.jpg"]
                          #"photo/photo2.jpg",
                          #"photo/photo3.jpg"]
                #i = random.randrange(0,3,1)
                fp = open(photos[0], "rb")
                file_info = InputFileInfo(photos[0], fp, 'image/jpg')
                a = InputFile('photo', file_info)
                self.bot.send_photo(chat.id, a)
                fp.close()
            #Send comment from Toxa.txt file
            if Toxa in text:
                fp = open("Toxa.txt")
                lines = fp.readlines()
                fp.close()
                i = random.randrange(0,len(lines)-1,1)
                slogan = (lines[i].strip())
                bot_answer = slogan + '\n'
                try:
                    self.bot.send_message(chat.id, bot_answer)
                except Exception:
                    self.bot.send_message(chat.id, 'Unknow error. Sorry.')
            #Send comment from Zaur.txt file
            if Zaur in text:
                fp = open("Zaur.txt")
                lines = fp.readlines()
                fp.close()
                i = random.randrange(0,len(lines)-1,1)
                slogan = (lines[i].strip())
                bot_answer = slogan + '\n'
                try:
                    self.bot.send_message(chat.id, bot_answer)
                except Exception:
                    self.bot.send_message(chat.id, 'Unknow error. Sorry.')
           #Send comment from Leha.txt file
            if Leha in text:
                fp = open("Leha.txt")
                lines = fp.readlines()
                fp.close()
                i = random.randrange(0,len(lines)-1,1)
                slogan = (lines[i].strip())
                bot_answer = slogan + '\n'
                try:
                    self.bot.send_message(chat.id, bot_answer)
                except Exception:
                    self.bot.send_message(chat.id, 'Unknow error. Sorry.')
           #Send comment from Igor.txt file
            if Igor in text:
                fp = open("igor.txt")
                lines = fp.readlines()
                fp.close()
                i = random.randrange(0,len(lines)-1,1)
                slogan = (lines[i].strip())
                bot_answer = slogan + '\n'
                try:
                    self.bot.send_message(chat.id, bot_answer)
                except Exception:
                    self.bot.send_message(chat.id, 'Unknow error. Sorry.')
           #Send comment from Pasha.txt 
