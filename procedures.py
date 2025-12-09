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

# Define Functions

def RUVerbProcedure(user_verb, verb_base):
    dict_form = user_verb
    stem_form = verb_base
    negative_form = conjugateRUNegative(verb_base=verb_base)
    past_negative_form = conjugatePastNegative(negative_v=negative_form)
    te_form = conjugateRUTEForm(verb_base=verb_base)
    past_form = conjugatePast(te_verb=te_form)
    polite_forms = conjugatePolite(verb_root=stem_form)
    conjugation_dict = {"Dictionary Form": dict_form, "Stem Form": stem_form, "Polite Form(s)": polite_forms, \
                        "Negative Form": negative_form, "Past Negative Form": past_negative_form, "Past Form": \
                            past_form, "Te Form": te_form}
    return conjugation_dict


def UVerbProcedure(user_verb, verb_base):
    dict_form = user_verb
    stem_form = conjugateUStem(user_verb=user_verb)
    negative_form = conjugateRUNegative(verb_base=verb_base)
    past_negative_form = conjugatePastNegative(negative_v=negative_form)
    te_form = conjugateUTEForm(user_verb=user_verb, verb_type="U")
    past_form = conjugatePast(te_verb=te_form)
    polite_forms = conjugatePolite(verb_root=stem_form)
    conjugation_dict = {"Dictionary Form": dict_form, "Stem Form": stem_form, "Polite Form(s)": polite_forms, \
                        "Negative Form": negative_form, "Past Negative Form": past_negative_form, "Past Form": \
                            past_form, "Te Form": te_form}
    return conjugation_dict

def IRVerbProcedure(user_verb): # This only covers the two most common irregular verbs. As noted, I am just one person. 
    dict_form = user_verb
    stem_form = conjugateIRStem(user_verb=user_verb)
    te_form = conjugateUTEForm(user_verb=user_verb, verb_type="IR")
    past_form = conjugatePast(te_verb=te_form)
    polite_forms = conjugatePolite(verb_root=stem_form)
    if user_verb == "する":
        negative_form = "しない"
    else:
        negative_form = "こない"
    past_negative_form = conjugatePastNegative(negative_v=negative_form)
    conjugation_dict = {"Dictionary Form": dict_form, "Stem Form": stem_form, "Polite Form(s)": polite_forms, \
                        "Negative Form": negative_form, "Past Negative Form": past_negative_form, "Past Form": \
                            past_form, "Te Form": te_form}
    return conjugation_dict
