import pyinputplus as pyip 
import random, time

def mutiply():
    nqs = 10
    score = 0
    for questionNumber in range(nqs):
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
        try:
            pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],blockRegexes=[('.*', 'Incorrect!')],
            timeout=8, limit=3)
        except pyip.TimeoutException:
            print('Too late !')
        except pyip.RetryLimitException:
            print('You have reached your retry limit !')
        else:
            print('Congratulations it\'s correct!!')
            score += 1
            time.sleep(1) 
            print('Score: %s / %s' % (score, nqs))