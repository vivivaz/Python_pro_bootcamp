#Write your code below this line 👇
def prime_checker(number):
    y = 0
    for i in range(1,10):
        if number % i == 0:
            y += 1
    if number==2 or number==3 or number==5 or number==7 or y < 2:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
