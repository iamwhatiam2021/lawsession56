number = input("give me a number please")
try:
    number = int(number)
except:
    print("that was not a number")
else:
    if number % 2 == 0:
        print("your number is even")
    else:
        print("your number is odd")