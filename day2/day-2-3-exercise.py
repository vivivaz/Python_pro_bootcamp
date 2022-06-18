# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#day = 1
#week = 7 
#month = 30
#year = 365
'''
age = int(age)
max_days = 90 * 365
max_week = (90*12)*4.3
max_month = 90*12

days_lived = age * 365
weeks_lived = age * 12 * 4.3
month_lived = age * 12

rest_days = max_days - days_lived
rest_months = max_month - month_lived
rest_weeks = max_week - weeks_lived
'''
age = int(age)
rest_years = 90 - age
rest_days = rest_years * 365
rest_months = rest_years * 12
rest_weeks = rest_years * 52


print(f"You have {rest_days} days, {rest_weeks} weeks and {rest_months} months to lived if you live until 90 years old.")
 







