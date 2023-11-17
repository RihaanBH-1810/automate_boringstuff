import re

def strip_word(word, rep=''):
    if rep == '':
        return re.sub(r'^\s+|\s+$', '', word)
    stripped_word = re.sub(f'^[\\{rep}]+|[\\{rep}]+$','', word)
    return stripped_word


print(strip_word(" Pessi     "))
print(strip_word("$$$$$Ronaldo is the goat!$$$$$$", '$'))