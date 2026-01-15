### Level 1
##Q1
# age = input("Enter your age: ")
# if int(age) >= 18:
#     print("You are old enough to drive.")
# else:
#     print(f"You need {18 - int(age)} more years to drive.")

##Q2
# my_age = 32
# your_age = input("Enter your age: ")
# if my_age > int(your_age):
#     print(f"I am {my_age - int(your_age)} years older than you.")
# elif my_age < int(your_age):
#     print(f"I am {int(your_age) - my_age} years younger than you.")
# else:
#     print("We are the same age.")

##Q3
# NumberOne = input("First, enter a number between 1-10.")
# NumberTwo = input("Second, enter a number between 1-10.")

# if NumberOne > NumberTwo:
#     print(f"{NumberOne} is greater than {NumberTwo}")
# elif NumberOne < NumberTwo:
#     print(f"{NumberOne} is smaller than {NumberTwo}")
# else:
#     print(f"{NumberOne} is equal to {NumberTwo}")

### Level 2
##Q1
# ```sh
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
# ```

grade = int(input("What was your score? "))
if grade >= 90:
    print("A")
elif grade >= 80 and grade <= 89:
    print("B")
elif grade >= 70 and grade <= 79:
    print("C")
elif grade >= 60 and grade <= 69:
    print("D")
else:
    print("F")