#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Eliza Program """
__author__="Sera Oraha"

#when questions get too hard, get in control of 
#the situation (ex: well, what do you think?)

import random
import re

q0="Why are you feeling "
q1="Tell me about your family."
q2="Tell me about your day."
q3="What do you want to do?"
q4="What are you doing right now?"

q = [q1,q2,q3,q4]

q5="What do you like to do with your "

def isGoodbye(text):
    laters = re.match(r'((see (you|ya) ?(later)?)|(laters?))',text,re.I)
    gb = re.match(r'.*bye.*',text,re.I)
    return (laters is not None) or (gb is not None)

def get_random_question(setofq):
    random.shuffle(setofq)
    return setofq[0]

def get_next_question(text):
    feels = re.match(r'(.*)?(good|joyful|happy|bad|sad|mad)(.*)?',text,re.I)
    rlshp = re.match(r'.*((mom|mother)|(dad|father)|(brother)|(sister)|(cousin)|(friend)).*',text,re.I)
    ing = re.match(r'(\w*)(?<!th)ing',text,re.I)
    
    response=""
    if feels is not None:
        response = q0 + str(feels.group(2)).lower() + "?"
    else:
        response = get_random_question(q)
        if rlshp is not None:
            q6 = "What does your " + (str(rlshp.group(1)).lower()) + " do for a living?"
            fam_q=[q5,q6]
            response = get_random_question(fam_q)
            if(response==q5):
                response = q5 + (str(rlshp.group(1)).lower()) +"?"
    return response


#constantly ask user for questions
#end when user says goodbye
def dialogue():    
    finished=False
    #inp for name
    print("Hello, what's your name?")
    name = input()
    print("Hello " + name + ". How are you today?" )
    inp_feeling = input()
    print(get_next_question(inp_feeling))
    while(not finished):
        user=input()
        finished=isGoodbye(user)
        if(finished is False):
            print(get_next_question(user))  

        
if __name__=="__main__":
    dialogue()


