def finder(target: int, num_list: list, start: int = 0, end: int = None) -> int:
    """
    this function finds the index of Target value
    in our desired list
    """
    if end == None:
        end = len(num_list) - 1
    
    if end == start:
        return None

    mid = (start + end) // 2

    if target == num_list[mid]:
        return mid
    elif target == num_list[start]:
        return start
    elif target == num_list[end]:
        return end
    elif target > num_list[mid]:
        return finder(target, num_list, (mid + 1), end)
    return finder(target, num_list, start, (mid - 1))


def binary_search(element: int, *args: int) -> int:
    """
    this function take the first argument as the target for
    binary search and the rest of arguments that given to the
    function with *args, make an range of number for search
    """
    my_list = [*args]
    return finder(element, my_list)