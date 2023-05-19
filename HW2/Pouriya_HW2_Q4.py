def fact(num: int) -> int:
    """
    this function take an integer number as input
    and calculates and return it's factorial value.
    """
    if num == 0 or num == 1:
        return 1
    else:
        return (num * fact(num - 1)) 


def neper(sent: int, expo: int) -> float:
    """
    this function calculates the exponent of Neper number
    for certain number of sentences and return a float
    number with 3 decimal places
    

    sent: number of sentences to calculate the exponent of
    neper number

    expo: amount of exponent
    """
    # make every sentence and put them into a list
    neper_values = [(expo ** i) / (fact(i)) for i in range(sent)]

    # then sum all the value of the list
    # and return the final answer with 3 decimal in places
    return (f'{sum(neper_values) :.3f}')


xy = neper(4,5)
print(xy)
print(type(xy))