import random

numberOfStreaks = 0
r_c_flip = []
repetitions = 0


for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    for i in range(100):
        r_c_flip.append(random.randint(0,1))
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(1, len(r_c_flip)-1):
        if(r_c_flip[i] == r_c_flip[i-1]):
            repetitions += 1
        else:
            repetitions = 0
        if repetitions == 6:
           numberOfStreaks += 1
    r_c_flip =[]
print('Chance of streak: %s%%' % (numberOfStreaks / 100))