#converts a string to a float value
def str_to_float(string:str) -> float:
    try:
        #trys to see if it makes conversion
        conversion = float(string)
        return conversion
    #Exception it was incable of translating the value and returns None
    except ValueError:
        return None
