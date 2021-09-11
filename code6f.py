#6. Return the BMI

def bmi():
    get_height = 0.0
    get_weight = 0.0
    bmi_index = 0.0

    get_height = float(input("Please enter your height in meters:"))
    get_weight = float(input("Please enter your weight in kilo:"))
    bmi_index = (get_weight)/(get_height)**2 
    if bmi_index < 18.5:

        print("You are underweight!")
    elif 18.5 <= bmi_index <= 24.9:

        print("You are normal!")
    elif bmi_index >= 25:
        print("You are overweight!!")
    else: print("Invalid")


bmi()




