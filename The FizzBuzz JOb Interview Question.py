# You are going to write a program that automatically prints the solution to the FizzBuzz game.

for number in range(1, 101):
    # We start off with this logic because we need to check for both numbers first
    # If we were to only check out 3 or 5 first then the if statement will have to print out the statement
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
