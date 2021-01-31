#Michael Gonzales
#1/15/2021
#Leap year check

i = 1

while i == 1:

    #error handle
    while True:
        try:
            year = int(input("enter year: "))
            break
        except ValueError:
            print("invalid number, try again.")

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{0} is a leap year".format(year))
            else:
                print("{0} is not a leap year".format(year))
        else:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))
        
    i = int(input("do you want to quit 1 = no, 0 = yes: "))
