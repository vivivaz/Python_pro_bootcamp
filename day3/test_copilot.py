def BMI_calculator():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    BMI = weight / (height ** 2)
    print("Your BMI is: ", BMI)
    if BMI < 18.5:
        print("You are underweight")
    elif BMI >= 18.5 and BMI < 25:
        print("You are normal")
    elif BMI >= 25 and BMI < 30:
        print("You are overweight")
    elif BMI >= 30:
        print("You are obese")
BMI_calculator()