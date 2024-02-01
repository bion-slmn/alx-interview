#!/usr/bin/python3
'''
defines a function to validate a sequence and valid utf-8 encoding
'''


def validUTF8(data):
    '''validate if the data passed is a utf8 encoding

    Parameter:
    data (list): list of intergers to determine if they are valid encoding

    Return:
    True if all are valid and False if any is not'''
    number_of_bytes = 0

    for val in data:
        if number_of_bytes > 0:
            if val >> 6 == 0b10:
                number_of_bytes = -1
            else:
                return False
        else:
            if val >> 7 == 0:
                number_of_bytes = 0
            elif val >> 5 == 0b110:
                number_of_bytes = 1
            elif val >> 4 == 0b1110:
                number_of_bytes = 2
            elif val >> 5 == 0b11110:
                number_of_bytes = 3
            else:
                return False
    return True
