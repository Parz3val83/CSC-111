# program to determine the user's bmi


# metric function to calculate bmi
def bmi_metric(weight_kg, height_m):
    usr_bmi_metric = weight_kg / (height_m ** 2)
    return usr_bmi_metric

# imperial function to caltulat bmi
def bmi_imp(weight_lb, height_in):
    usr_bmi_imp = 703 * (weight_lb / (height_in ** 2))
    return usr_bmi_imp


# define variable weight class to store bmi ranges
weight_class = ""
# get user input for measrument system
usr_sys = input("What is your prefered system of measurement?\n(imperial or metric): ")
# get user input for weight
usr_weight = float(input("Enter is your current weight: "))
# get user input for height
usr_height = float(input("Enter your current height: "))

# define variable to store bmi value
bmi = -1.0

# use if-else to determine usr prefered system of measurement
if usr_sys == "metric":
    bmi = bmi_metric(usr_weight, usr_height)
    print("Your BMI is", bmi)
elif usr_sys == "imperial":
    bmi = bmi_imp(usr_weight, usr_height)
    print("Your BMI is", bmi)
else:
    print("Error, enter a correct system.")

# use if series to determine user weight class range
if bmi > 0 and bmi < 15:
    weight_class = "very severly underweight"
if bmi >= 15 and bmi < 16:
    weight_class = "severely underweight."
if bmi >= 1 and bmi < 18.5:
    weight_class = "under weight."
if bmi >= 18.5 and bmi < 25:
    weight_class = "normal (healthy weight."
if bmi >= 25 and bmi < 30:
    weight_class = "overweight."
if bmi >= 30 and bmi < 35:
    weight_class = "obese class I (moderately obese)."
if bmi >= 35 and bmi < 40:
    weight_class = "obese class II (severely obese)."
if bmi >= 40:
    weight_class = "obese class III (very severely obese)."

# format and output user bmi
print("and you are conssidered", weight_class)
