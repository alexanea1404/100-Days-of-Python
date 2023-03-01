
print("Welcome to the tip calculator")
total_bill = float(input("What is the total bill?\n$ "))
tip_percent = float(input("How much tip would you like to give? 10, 12 or 15 %\n "))
total_people = float(input("How many people split the bill? "))

total_per_person = total_bill/total_people
tip_per_person = total_per_person*tip_percent/100

total_per_person += tip_per_person

print("Each person should pay {:.2f}".format(total_per_person))

