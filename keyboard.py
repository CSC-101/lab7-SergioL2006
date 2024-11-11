from convert import str_to_float

#function to gather all numbers inputed into a list
def gathered_numbers() -> float:
    #Used as placeholder to repeat
    repeat = 1
    holder = 0
    #Repeats infinitely until user decides to finish by typing done
    while repeat == 1:
        #input of user
        x = input()
        #checks if it was a integer put in and not 'None' from str_to_float function then adds onto one another
        if type(str_to_float(x)) == float:
            holder += str_to_float(x)
        #when 'done' is typed the functions returns added values
        elif x == 'done':
            return holder

    return holder

if __name__ == '__main__':
    print("Enter a numbers, type 'done' to stop")
    print(gathered_numbers())
