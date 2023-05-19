def apply_discount(price: int, discount: float = 0.0) -> int | None: 
    """
    Apply Discount Percent and Calculate Final Price

    Args:
        price: an integer number 
        discount: a float number between 0.0 and 1.0 
                  and has default value = 0.0

    Returns:
        int: return an integer number as final price
             that decreased by discount percent
        None: return None when take discount amount 
              equal or bigger than 1
    """

    final_price = int(price * (1 - discount)) 
    if 0 < final_price <= price:
        return final_price
    print("enter Discount Amount in range 0 to 1 !!!!")
    return None
    

if __name__ == "__main__":
    print(apply_discount(7500, 0.56))
    print(apply_discount(700, 0.7))
    print(apply_discount(500, 1))

"""
assert (
     0 < final_price <= price,
     'Why this AssertionError never Raised!' 
     )

    If the statement in front of ASSERT will be True,
the AssertionError never activate
and because in code in above, in front of assert there is a
tuple that is not empty, this tuple consider as True value
and never let the AssertionError get active!!!


    Using assertion is not a good way to validate data !!!
And it is better to use assertion only in cases of testing 
and troubleshooting
Because with -O command in the terminal, you can disable Assert!
"""
