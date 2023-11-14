spam = ['cat', 'dog', 'monkey', 'dog']
out_str = ''
for index , item in enumerate(spam):
    if index == 0:
        out_str += item 
    elif index > 0 and index < len(spam)-1:
        out_str = out_str + ', ' + item
    elif index == len(spam)-1:
        out_str = out_str + ', and ' + item
print(out_str)