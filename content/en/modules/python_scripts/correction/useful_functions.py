def change_case(string):
    if len(string) > 0:
        new_string = string[:-1].lower() + string[-1].upper()
    else:
        new_string = ""
    return new_string

def get_words(string):
    return string.split(" ")

def join_words(string_list):
    new_string = ""
    for word in string_list:
        new_string += word + " "
    new_string = new_string[:-1] # remove last space
    return new_string
