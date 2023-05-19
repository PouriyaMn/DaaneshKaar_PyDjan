def is_valid_postcode(string: str) -> bool:
    """
    this function take a string as input and check is that string
    valid or not for being a postal code and return a boolian value.
    """
    if len(string) == 11 and string.find("-") > 0 :
        code_list = string.split("-")
        len1 = len(code_list[0])
        len2 = len(code_list[1])
        isdigit1 = code_list[0].isdigit()
        isdigit2 = code_list[1].isdigit()
        
        if len1 == 5 and len2 == 5 and isdigit1 and isdigit2:
            return True
        return False
    return False


num = int(input('How Many Postcode Do You Want To Check: [enter a number]'))
input_list = [input(f'Enter Postcode No.{i+1}: ') for i in range(num)]

valid_postal_code = list(filter(is_valid_postcode, input_list))

print('\nIn Below We Have List of Valid PostCode'\
      , valid_postal_code, sep="\n")