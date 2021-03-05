try:
    age = input('How old are you?')
    # we try to convert the age to the number
    age = int(age)
except ValueError:
    print("Sorry, but that was not a number")
except ZeroDivisionError:
    print("Can not divide by zero")
except:
    print("Something Else Happened")
else:
    print("you were born around", 2021-age)
finally:
    print("Thanks for playing my game")
