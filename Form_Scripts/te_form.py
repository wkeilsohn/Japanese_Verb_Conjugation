# William Keilsohn
# December 4 2025

# Define Variables
te_irregulars = {"いく":"いって", "くる":"きて", "する":"して"}
te_u_regulars = {"く":"いて", "ぐ":"いで", "す":"して", "る":"って", "つ":"って", "う":"って", "む":"んで", "ぬ":"んで", "ぶ":"んで"} # There may be a better way to organize this later.
te_r_regulars = {"る":"て"}
polite_add_on = "い"

# Define Functions

def conjugateTEForm(verb_base, verb_type): # This only makes the regular te_form. Not one of the polite derivatives. 
    global te_irregulars
    # global te_r_regulars # Not Necessary 
    global te_u_regulars
    te_verb = ""
    end_char = "" # Just allocating the variable as a reminder
    if verb_type == "RU":
        te_verb = te_verb + verb_base + "て"
        return te_verb
    else:
        change_char = verb_base[-1]
        verb_base = verb_base[:-1] # Remove the last character
        if verb_type == "IR":
            end_char = te_irregulars.get(change_char)
        else:
            end_char = te_u_regulars.get(change_char)
        te_verb = te_verb + verb_base + end_char
        return te_verb
        
def add_polite_glue(te_form_verb):
    global polite_add_on
    return te_form_verb + polite_add_on