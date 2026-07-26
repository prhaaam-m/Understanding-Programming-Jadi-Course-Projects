
#BMI Control Version 1
ques = "Y"
while ques != "N":
    weight = int(input("Please Enter Your Weight in KG: "))
    height = float(input("Please Enter Your Height in Meter: "))

    bmi = weight / (height ** 2)

    print(f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")

    ques = input("Wanna Do That Again: (Y or N) ").strip().upper()