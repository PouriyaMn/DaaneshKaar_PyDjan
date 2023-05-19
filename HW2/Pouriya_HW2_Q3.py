def sum_digit(num: int) -> int:
    """
    this function sum all digits of a number with
    each other till the final number get smaller 
    than 10 and return one digit number
    """
    num_digit = [int(n) for n in str(num)]
    summed = sum(num_digit)
    if summed >= 10:
        return sum_digit(summed)
    return summed


# print(sum_digit(1995))
# print(sum_digit(1374))
# print(sum_digit(1774))
# print(sum_digit(1751374))
# print(sum_digit(881995))