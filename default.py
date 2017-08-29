################################################################################
'''
File: default.py
Author: Ching-Yu Chen

Description:
default.py contains Default class, which is a program object of the "/default" 
command. Default pgm is the standby running program.

Copyright (c) 2017 Ching-Yu Chen
'''
################################################################################

import abc
import telepot   
import telebot
from telebot import types
from pgmabstract import PgmAbstract

################################################################################

class Default(PgmAbstract):
    
    ''' 
    "/default" command program. Ask the user to send current location or choose 
    the favorite locations. Then use the respond message to find and send the 
    station information. The default program is the standby running program.
    '''

    name = "/default"
    
    
    # enum of the state of the program

    START = 0
    RESPOND = 1
    END = -1


#-------------------------------------------------------------------------------

    def check_start(self, msg=None):
        return True

#-------------------------------------------------------------------------------

    def state_start(self, user, msg=None, args=None):
        
        '''
        The start state function. Return enum of the next state function and args. 
        '''

        markup = types.ReplyKeyboardMarkup(row_width=1)
        itembtn1 = types.KeyboardButton('opt1')
        itembtn2 = types.KeyboardButton('opt2')
        markup.add(itembtn1)
        markup.add(itembtn2)
        self.tb.send_message(user, "Choose a option", \
            reply_markup=markup)

        return [Default.RESPOND, args]

#-------------------------------------------------------------------------------

    def check_respond(self, msg):

        '''
        Return true if the respond message for the request state function from 
        the user is valid. Otherwise, return false.
        '''

        content_type, chat_type, chat_id = telepot.glance(msg)
        
        if content_type is 'text':
            if msg['text'] == 'opt1' or msg['text'] == 'opt2':
                return True
            else:
                return False
        else:
            return False

#-------------------------------------------------------------------------------

    def state_respond(self, user, msg, args=None):

        '''
        The respond state function. Return enum of the end state function and args.
        '''

        '''
        code implemented here
        '''
        
        return [Default.END, args]
        

#-------------------------------------------------------------------------------    
    
    def __init__(self):

        '''
        The Default Class is initialized so the command execution will be 
        operated by the bot and the tb object (telepot and telebot 
        object) initiated in superclass. Each state corresponding execute 
        function and check function are specified.
        '''

        self.statefun = [self.state_start, self.state_respond]
        self.check_cmd = [self.check_start, self.check_respond]
        super().__init__()
        

################################################################################

if __name__ == "__main__":
    
    ''' 
    For testing
    '''
   
    default_class = Default()

