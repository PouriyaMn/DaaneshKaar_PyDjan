changer = {
    'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6',
    'seven':'7', 'eight':'8', 'nine':'9', 'ten':'10', 'eleven':'11',
    'twelve':'12', 'thirteen':'13', 'fourteen':'14', 'fifteen':'15',
    'sixteen':'16', 'seventeen':'17', 'eighteen':'18',
    'nineteen':'19', 'twenty':'20',
}

with open('Zen.txt', 'r',) as f:
    my_txt = f.read()

letters_number = list(changer.keys())

# iterate wise-verse to prevent make fourteen to 4teen and others
# and first make fourteen to 14 and then four to 4
for l in letters_number[::-1]:
    my_txt = my_txt.replace(l, changer[l])

with open('newZen.txt', 'w') as f:
    f.write(my_txt)
