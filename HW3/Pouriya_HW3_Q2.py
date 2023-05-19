from math import inf


def divider(a: str | int | float,
            b: str | int | float) -> float | None:
    """
    this function wrote with EAFP style
    and take two number, even string type as input
    and return answer of dividing operation

    Args:
        a >>> could be one of (str | int | float)
        b >>> could be one of (str | int | float)
    
    Returns:
        float: return a float number as answer in correct cases
            or return a float type infinity as answer in ZeroDivision cases
        None: return a None as answer in other incorrect cases
    """
    try:
        div = float(a) / float(b)
    except ZeroDivisionError:
        print("ZeroDivisionError: division by !!ZERO!!")
        return inf
    except Exception as e:
        print("!!!Error!!!:", e)
        return None
    else:
        return div


if __name__ == "__main__":
    a, b = input('enter two numbers: ').split()
    print(divider(a, b))
