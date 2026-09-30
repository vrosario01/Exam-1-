def palindrome(string):
    ### add your solution here, including a docstring
    """
    string -> True/False
    this function takes in  a string and returns true if it is a palindrome, false otherwise
>>> palindrome("A man, a plan, a canal, Panama")
True
>>> palindrome("was it a rat I saw")
True
>>> palindrome("Never a foot too far, even")
True
    """
    string = string.strip().lower()
    cleaned_string = ""
    for i in string:
        if i.isalpha():
            cleaned_string = cleaned_string + i

    string = cleaned_string

    if string == string[::-1]:
        return True
    else:
        return False