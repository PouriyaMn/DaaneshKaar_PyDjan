n = int(input('enter the number of your test case : '.title()))

laptop_price_quality = {}
for i in range(n):
    p, q = input('enter the price & quality in order : '.title()).split()
    laptop_price_quality[int(p)] = (int(q))

max_price = max(laptop_price_quality.keys())
max_quality = max(laptop_price_quality.values())


# print(laptop_price_quality[max_price])
# print(max_quality)
print('Not Found' if laptop_price_quality[max_price] == max_quality else 'Founded')
