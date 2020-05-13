# -*- coding: utf-8 -*-
"""
Created on Thu May 14 03:28:19 2020

@author: Abhijit Mukherjee
"""

!pip install chatterbot

!pip install chatterbot_corpus

from chatterbot import ChatBot

from chatterbot.trainers import ChatterBotCorpusTrainer

bot= ChatBot('Siri')

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

print(bot.get_response("Where are you from"))

print(bot.get_response("Tell me about AI"))

print(bot.get_response("Tell me about yourself"))

print(bot.get_response("Will you be my Friend"))

print(bot.get_response("Do you have any friend?"))

print(bot.get_response("you don't know anything"))

print("Bot: Hello User!!")
print("Bot: My name is Siri :)")
print("Bot: Let's chat :)")
while True:
   user_input=input("You: ")
   if user_input=='bye' or user_input=='Bye':
     break
   else :
     bot_response = bot.get_response(user_input)
     print("Bot:",bot_response)

print("Bot: Bye")


