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

# grade = int(input("What was your score? "))
# if grade >= 90:
#     print("A")
# elif grade >= 80 and grade <= 89:
#     print("B")
# elif grade >= 70 and grade <= 79:
#     print("C")
# elif grade >= 60 and grade <= 69:
#     print("D")
# else:
#     print("F")

##Q2
# month = input("What month is it? ")
# if month in ("September, October, November"):
#     print("Autumn")
# elif month in ("December, January, February"):
#     print("Winter")
# elif month in ("March, April, Mary"):
#     print("Spring")
# elif month in ("June, July, August"):
#     print("Summer")
# else:
#     print("That is not a month!")

##Q3
# fruits = ['banana', 'orange', 'mango', 'lemon']
# newFruit = input("Can you name me a fruit? ")
# if newFruit not in fruits:
#     fruits.append(newFruit)
#     print(fruits)
# else:
#     print("That fruit already exists in my list." + str(fruits))

### Level 3
##Q1

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': 
    # ['JavaScript', 'React']
    ['Node', 'Python', 'MongoDB']
    # ['React', 'Node', 'MongoDB']
    # {'Node', 'MongoDB', 'Python'} "Trying for unordered."
,
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
        }
    }

if 'skills' in person.keys():
    print(person['skills'][round(len((person['skills']))/2)])
    if 'Python' in person['skills']:
        print("Person has skills in Python.")
if person['skills'] == ['JavaScript', 'React']:
    print('He is a front end developer.')
elif ['Node', 'Python', 'MongoDB'] == person['skills']:
    print('He is a backend developer.')
elif ['React', 'Node', 'MongoDB'] == person['skills']:
    print('He is a fullstack developer.')
else:
    print('unknown title')
if person['is_married'] == True and person['country'] == 'Finland':
    print('Asabeneh Yetayeh lives in Finland. He is married.')