# William Keilsohn
# December 8th 2025

####
# I don't like putting all this code in the main file.
####

# Import Packages
import os
import pandas as pd

## Import Custom Scripts
from Form_Scripts.te_form import *
from Form_Scripts.polite_form import *
from Form_Scripts.negative_form import *
from Form_Scripts.stem_form import *
from Form_Scripts.past_form import *

# Declare Variables
## This is more so here to reminde me which forms I need
dict_form = ""
te_form = ""
negative_form = ""
past_negative_form = ""
past_form = ""
stem_form = ""
polite_forms = []
conjugation_dict = {}

# Define Functions

def RUVerbProcedure(user_verb, verb_base):
    global dict_form
    global te_form
    global negative_form
    global past_negative_form
    global past_form
    global stem_form
    global polite_forms
    global conjugation_dict
    dict_form = user_verb
    stem_form = verb_base
    negative_form = conjugateRUNegative(verb_base=verb_base)
    past_negative_form = conjugateRUPastNegative(negative_ru=negative_form)
    te_form = conjugateTEForm(verb_base=verb_base, verb_type="RU")
    past_form = conjugatePast(te_verb=te_form)
    polite_forms = conjugatePolite(verb_root=stem_form)
    conjugation_dict = {"Dictionary Form": dict_form, "Stem Form": stem_form, "Polite Form(s)": polite_forms, \
                        "Negative Form": negative_form, "Past Negative Form": past_negative_form, "Past Form": \
                            past_form, "Te Form": te_form}


def UVerbProcedure(user_verb, verb_base):
    global dict_form
    global te_form
    global negative_form
    global past_negative_form
    global past_form
    global stem_form
    global polite_forms
    global conjugation_dict
    dict_form = user_verb
    stem_form = conjugateUStem(user_verb=user_verb)
    negative_form = conjugateRUNegative(verb_base=verb_base)
    past_negative_form = conjugateUNegativePast(negative_u=negative_form)
    te_form = conjugateTEForm(verb_base=verb_base, verb_type="U")
    past_form = conjugatePast(te_verb=te_form)
    polite_forms = conjugatePolite(verb_root=stem_form)
    conjugation_dict = {"Dictionary Form": dict_form, "Stem Form": stem_form, "Polite Form(s)": polite_forms, \
                        "Negative Form": negative_form, "Past Negative Form": past_negative_form, "Past Form": \
                            past_form, "Te Form": te_form}
