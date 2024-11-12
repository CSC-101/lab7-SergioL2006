import sys
from convert import str_to_float

def main():
    #placeholder for total
    total = 0
    #begins at first index to end
    for arg in sys.argv[1:]:
        #used to check the inputs if it is a string or not
        number = str_to_float(arg)
        #if the value is a float value, it will add on
        if number == float:
            total += number
    #prints total values added upon one another
    print("The values sum is: ", total)

if __name__ == '__main__':
    main()
