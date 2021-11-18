def Grade_Percentage():
    Percentage = float(input("Enter your Grade Percentage here: "))

    if Percentage >= 97 and Percentage <= 100:
        print("Grade/Mark: 1.0")
        print("Description: Excellent")
    elif Percentage >= 94 and Percentage <= 96:
        print("Grade/Mark: 1.25")
        print("Description: Excellent")
    elif Percentage >= 91 and Percentage <= 93:
        print("Grade/Mark: 1.5")
        print("Description: Very Good")
    elif Percentage >= 88 and Percentage <= 90:
        print("Grade/Mark: 1.75")
        print("Description: Very Good")
    elif Percentage >= 85 and Percentage <= 87:
        print("Grade/Mark: 2.0")
        print("Description: Good")
    elif Percentage >= 82 and Percentage <= 84:
        print("Grade/Mark: 2.25")
        print("Description: Good")
    elif Percentage >= 79 and Percentage <= 81:
        print("Grade/Mark: 2.5")
        print("Description: Satisfactory")
    elif Percentage >= 76 and Percentage <= 78:
        print("Grade/Mark: 2.75")
        print("Description: Satisfactory")
    elif Percentage == 75:
        print("Grade/Mark: 3.0")
        print("Description: Passing")
    elif Percentage >= 65 and Percentage <= 74:
        print("Grade/Mark: 5.0")
        print("Description: Failure")
    else:
        print("Grade/Mark: Inc.")
        print("Incomplete")

Equivalent = Grade_Percentage()