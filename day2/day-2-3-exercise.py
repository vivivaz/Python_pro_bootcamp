# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age = int(age)
rest_years = 90 - age
rest_days = rest_years * 365
rest_months = rest_years * 12
rest_weeks = rest_years * 52


print(f"You have {rest_days} days, {rest_weeks} weeks and {rest_months} months to lived if you live until 90 years old.")
 