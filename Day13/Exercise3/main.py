for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
  
#Bug fixed:
#Line 2: "and" instead of "or"
#Line 4: elif instead of if
#Line 6: elif instead of if
