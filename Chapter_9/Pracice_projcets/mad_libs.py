from pathlib import Path
file = open(Path.cwd()/'mad.txt', 'r')
text = file.read()
file.close()

adj = input("Enter an adjective : ")
noun = input("Enter a noun : ")
verb = input("Enter a verb : ")
noun2 = input("Enter a noun : ")

text = text.replace('ADJECTIVE', adj)
text = text.replace('NOUN', noun, 1)
text = text.replace('VERB', verb)
text = text.replace('NOUN', noun2)

file = open(Path.cwd()/'mad.txt', 'w')
file.write(text)
file.close