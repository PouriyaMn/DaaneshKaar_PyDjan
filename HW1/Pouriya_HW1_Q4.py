txt = input("enter your desired string: ".title())
"""
this program is Case Sensitive!
for Case Insensitive option you could use code below
instead of first line

>>> txt = input("enter your desired string: ".title()).lower()

"""

letters = []

for i in txt:
    if i not in letters:
        letters.append(i)

my_dict = {}
for l in letters:
    my_dict[l] = txt.count(l)

print(my_dict)
