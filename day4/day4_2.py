# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

tam = len(names)
num = random.randint(0, tam-1)
pay = names[num]
print(f"{pay} is going to buy the meal today!")
