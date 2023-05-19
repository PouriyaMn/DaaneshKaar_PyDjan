n = int(input('enter the number of your test case : '.title()))

laptop_quality_price = {}
for i in range(n):
    p, q = input('enter the price & quality in order : '.title()).split()
    laptop_quality_price[int(q)] = (int(p))


laptop_quality = laptop_quality_price.keys()

RedFlag = 'down'
#compare each laptop quality with other laptops quality
for QUALITY in laptop_quality:
    # and make a list with price of higher quality laptops
    higher_qualityPrice = [laptop_quality_price[q] for q in laptop_quality if q > QUALITY ]

    PRICE = laptop_quality_price[QUALITY]
    
    # list the HIGHER QUALITY with LESS PRICE >>> HQLP
    hqlp = list(filter(lambda x : x < PRICE, higher_qualityPrice))
    
    #if could find a laptop with higher quality but less price, the HQLP list length would be more than ZERO (!=0)
    if len(hqlp) > 0:
        RedFlag = 'UP'

if RedFlag == 'UP':
    print('Founded')
else:
    print('Not Found')