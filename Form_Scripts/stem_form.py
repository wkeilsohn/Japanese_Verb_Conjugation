# William Keilsohn
# December 8th 2025

# Import Packages
import os
import pandas as pd


# Declare Variables

cpath = os.getcwd() 
files_location = os.path.join(cpath, "Charts")
char_file = os.path.join(files_location, "chars.csv")
chars_df = pd.read_csv(char_file)

# Define Functions

def conjugateRUStem(verb_base): # This is a useless endeavore for RU verbs.
    return verb_base 

def conjugateUStem(user_verb):
    global chars_df
    new_verb = user_verb[:-1]
    new_end_char = chars_df.loc[chars_df['U'] == "う", 'A'].iloc[0]
    return new_verb + new_end_char