def cels_to_fahr(temp: int | float) -> float:
    """
    this function turns a celsius temperature to fahrenheit
    
    temp(C) ---> temp(F)
    """
    fahr = (temp * (1.8)) + 32
    return float(f'{fahr:.2f}')


n = int(input('How many test case do you have: [enter a number] '))

celsius = [float(input(f'Enter your test case No.{i+1}: ')) for i in range(n)]
print(f'\nThe Celsius Temperature List:\n{celsius}')

fahrenheit = list(map(cels_to_fahr, celsius))
print(f'\nThe Fahrenheit Temperature List:\n{fahrenheit}')
