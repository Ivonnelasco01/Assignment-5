def life_stage():
    age = int(input("Age: "))

    if age >= -1 and age <= 12:
        print("Kid")
    elif age >= 13 and age <= 17:
        print("Teen")
    elif age == 18:
        print("Debut")
    elif age >= 19:
        print("Adult")

lifeStage = life_stage()