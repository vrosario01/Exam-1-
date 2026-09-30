
def funct_applied_to_list(list, funct):
    """ 
    ## don't forget the docstring which doesn't count in line count
    list -> (list)**2
    this function takes in a list and a function and applies a function that squares each item in the list
    >>> funct_applied_to_list([1,2,3,4,6], lambda x: x ** 2)
    [1, 4, 9, 16, 36]
    >>> funct_applied_to_list([2,4,6,8], lambda x: x ** 2)
    [4, 16, 36, 64]
    >>> funct_applied_to_list([2,2,2,2,7], lambda x: x ** 2)
    [4, 4, 4, 4, 49]
    """
    return [funct(x) for x in list]
print(funct_applied_to_list([2,2,2,2,7],lambda x: x ** 2))


