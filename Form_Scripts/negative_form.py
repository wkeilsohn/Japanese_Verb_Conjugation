# William Keilsohn
# December 8th 2025

# Import Packages
import pandas as pd
import os

cpath = os.getcwd() 
files_location = os.path.join(cpath, "Form_Scripts\Charts")
char_file = os.path.join(files_location, "chars.csv")
chars_df = pd.read_csv(char_file)

present_ending = "ない"
past_ending = "かった"

# Declare Functions

def conjugateRUNegative(verb_base):
    global present_ending
    return verb_base + present_ending

def conjugateRUPastNegative(negative_ru):
    global past_ending
    return negative_ru[:-1] + past_ending

def conjugateUNegative(user_verb):
    global chars_df
    global present_ending
    new_verb = user_verb[:-1]
    if user_verb[-1] == "う":
        new_end_char = "わ"
    else:
        new_end_char = chars_df.loc[chars_df['U'] == "う", 'A'].iloc[0]
    return new_verb + new_end_char + present_ending

def conjugateUNegativePast(negative_u):
    global past_ending
    new_verb = negative_u[:-1]
    return new_verb + past_ending