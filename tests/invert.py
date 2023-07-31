
def invert_case(string):
    '''
    invert_case("hexlet")
    invert_case("HEXLET")
    invert_case("Thsis")
   '''

  

    result = ''
    for char in string:
        result += char.swapcase()
    return result


if __name__ == "__main__":
    import doctest
    failed, attempted = doctest.testmod()
    assert failed == 0
    assert attempted == 3