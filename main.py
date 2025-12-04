# William Keilsohn
# December 3 2025

# Import Packages
import os
import numpy as np
import pandas as pd

## Import Custom Scripts
from Form_Scripts.te import *

# Delcare Global Variables
ru_verb_end_char = "る"
irreg_ls = ["する", "くる"]
exception_ls = ["ある", "いく"]

path = os.getcwd()


# Define Functions

def takeVerb():
    user_verb = input("Please Enter a Verb: ")
    return user_verb

def exceptionVerbChecker(user_verb):
    is_exception = False
    if user_verb in irreg_ls:
        is_exception = True
    elif user_verb in exception_ls:
        is_exception = True
    return is_exception

def ruVerbChecker(user_verb):
    # Expand this later
    print("May be an RU Verb")

def verbChecker(user_verb, end_char):
    ru_verb_status = False
    if end_char == ru_verb_end_char:
        ru_verb_status = ruVerbChecker(user_verb)
    return ru_verb_status


# Run Application

if __name__=="__main__":
    ru_verb_status = False
    user_verb = takeVerb()
    verb_base = user_verb[:-1]
    end_char = user_verb[-1]
    exception_status = exceptionVerbChecker(user_verb=user_verb)
    if exception_status:
        print("Exception Look Up Procedue") # TBD
    else:
        ru_verb_status = verbChecker(user_verb=user_verb, end_char=end_char)
        if ru_verb_status:
            print("RU Verb Status Procedure") #TBD
        else:
            print("U Verb Status Procedure") #TBD
