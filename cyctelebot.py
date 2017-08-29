#!/usr/bin/env python3
################################################################################
'''
File: cyctelebot.py
Author: Ching-Yu Chen

Description:
cyctelebot.py contains a CYCTelebot class which is a telegram bot object. The 
object communicates and executes the commands from the telegram users.

Copyright (c) 2017 Ching-Yu Chen
'''
################################################################################

import telepot     
from telepot.loop import MessageLoop
from time import sleep
from cmdanalyzer import *

################################################################################

class CYCTelebot:

    '''
    CYCTelebot is a telebot object that communicates and executes the 
    commands from the telegram users. The list of commands are in the 
    commandsmap.json.
    '''
    
#-------------------------------------------------------------------------------

    def __init__(self):

        try:
            TOKEN = ""
            with open('Token', 'r') as f:
                TOKEN = f.read().strip()
            f.close()
            assert(len(TOKEN) != 0)
        except:
            print("Token file doesn't exit or invalid token")


        try:
            # The telepot object that receives and send message
            self.bot = telepot.Bot(TOKEN)
            assert(self.bot != None)
        except:
            print("problem initializing bot. Token invalid or telepot is not operating")

        
        # The CmdAnalyzer object analyze the received commands
        self.cmdanalyzeri = CmdAnalyzer()

#-------------------------------------------------------------------------------

    def handle(self, msg):
        
        ''' 
        Handle the received msg. If the msg is a command than execute the 
        command. Otherwise send a message of "not a command".
        '''

        content_type, chat_type, chat_id = telepot.glance(msg)
        
        if self.cmdanalyzeri.is_command(msg): 
            self.cmdanalyzeri.execute(chat_id, msg)
        else:
            self.bot.sendMessage(chat_id, 'Not a valid command. Please retype '
                'the command or type /help for command instructions.')
       
                
#-------------------------------------------------------------------------------

    def run(self):

        '''
        Run the CYCTelebot object. Starts handling the received messages from 
        the telegram users.
        '''

        MessageLoop(self.bot, self.handle).run_as_thread()

        while True:
            sleep(3)

################################################################################

if __name__ == "__main__":

    '''
    The main function initiate a CYCTelebot object and runs it.
    '''
    
    testclass = CYCTelebot()
    testclass.run()
    
