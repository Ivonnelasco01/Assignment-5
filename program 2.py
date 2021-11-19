def low_num():
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    num3 = int(input("Enter 3rd number: "))
    min = num1
    if num2 < min:
        min = num2
    elif num3 < min:
        min = num3
    print(min,"is the smallest number")
lowestNumber = low_num()

