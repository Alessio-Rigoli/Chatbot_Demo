######################################################
# RMIT Project: Chatbot program                      #
# Team: AAV (Advanced Academy of Voice Assistants)   #   
# By Alessio, Vignesh & Anton                        #
# Written on the 8th of Febuary 2020                 #   
######################################################

#!/usr/bin/python3
#Import all necessary modules
import time
import nltk
import os
import numpy as np
import random
import string

from nltk.chat.util import Chat, reflections
pairs = [[r"my name is (.*)", ["Hello %1. How are you going today?"]],
#Displays the current time in a readable format (Date, Month and current time)
localtime = time.asctime( time.localtime(time.time()) )
print (localtime)

def firstChatBot()):
    print("Hi I am the CHATBOT here to assist, the current time is:", localtime)
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == '__main__':
    firstChatBot()
