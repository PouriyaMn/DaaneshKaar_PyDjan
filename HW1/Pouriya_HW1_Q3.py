txt = input('enter your sentence : '.capitalize())
txt = txt.replace(' ','')

vowels_list = ['a','e','i','o','u','A','E','I','O','U']

for vowel in vowels_list:
    if vowel in txt:
        txt = txt.replace(vowel,'.')

print(txt.swapcase())
