from datetime import datetime
import jdatetime

def second_since_birth(birthdate: str) -> int:
    """
    calculate total seconds that past since the birth date.

    Args:
        birthdate (str): take a string argument as input
                         with YYYY-MM-DD format 

    Returns:
        int: return an integer number that show how many seconds past
             since the birth date
    """
    birth_date = datetime.strptime(birthdate, "%Y-%m-%d")
    current_date = datetime.today()

    delta = current_date - birth_date
    total_seconds = delta.total_seconds()

    return int(total_seconds)


def next_birthday(birthdate: str) -> tuple[int, int]:
    """
    calculate the total days and minutes left to the next birthday

    Args:
        birthdate (str): take a string argument as input
                         with YYYY-MM-DD format

    Returns:
        tuple[int, int]: return a tuple that it's 
                         FIRST index show an integer as DAYs and
                         SECOND index show an integer as MINUTEs
                         that left to the next birthday
    """

    birth_date = datetime.strptime(birthdate, "%Y-%m-%d")
    current_date = datetime.today()

    next_birthday = datetime.strptime(
        f"{current_date.year}-{birth_date.month}-{birth_date.day}",
        "%Y-%m-%d"
        )
    next_delta = next_birthday - current_date

    if (next_delta.total_seconds()) >= 0:
        return next_delta.days, (next_delta.seconds // 60)
        
    next_birthday = datetime.strptime(
        f"{current_date.year + 1}-{birth_date.month}-{birth_date.day}",
        "%Y-%m-%d"
        )
    next_delta = next_birthday - current_date
    return next_delta.days, (next_delta.seconds // 60)


def persian_date(gregorian_date: str) -> str:
    """
    Convert Shamsi date to Gregorian

    Args:
        gregorian_date (str): take a string argument as input
        with YYYY-MM-DD format

    Returns:
        str: return a string that show shamsi date with YYYY-MM-DD format
    """
    g_date = datetime.strptime(gregorian_date, "%Y-%m-%d")
    p_date = jdatetime.date.fromgregorian(
        year = g_date.year,
        month = g_date.month,
        day = g_date.day,
    )
    return str(p_date)


if __name__ == "__main__":
    input_birth_date = input('enter your birth date like sample [Year-Month-Day]: ')

    seconds = second_since_birth(input_birth_date)
    countdown = next_birthday(input_birth_date)
    persian = persian_date(input_birth_date)

    print("\nTotal seconds passed since your birth:", seconds)
    print(f"\n{countdown[0]} day(s) & {countdown[1]} minute(s) Left to the next Birthday ^__^")
    print("\nYour Birthday in persian calender >>>",persian)
