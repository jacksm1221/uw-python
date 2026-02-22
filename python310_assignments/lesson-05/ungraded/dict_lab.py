d = {
    "name": "Chris",
    "city": "Seattle",
    "cake": "chocolate"
}

# Part 1
'''
    Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”. So the keys should be: “name”, etc, and values: “Chris”, etc.

    Display the dictionary.

    Delete the entry for “cake”.

    Display the dictionary.

    Add an entry for “fruit” with “Mango” and display the dictionary.

            Display the dictionary keys.

            Display the dictionary values.

            Display whether or not “cake” is a key in the dictionary (i.e. False) (now).

            Display whether or not “Mango” is a value in the dictionary (i.e. True).
'''
print(d)
d.pop("cake")
print(d)
d.update({"fruit": "mango"})
print("mango" in d.values())
print(d)

# Part 2
'''Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value as the value (consider upper and lower case?).'''
d2 = {}
for key, value in d.items():
    d2.update({key: value.count("t")})
print(d2)

# Part 3
'''
    Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4. Figure out a way to compute those – don’t just type them in.

    Display the sets.

    Display if s3 is a subset of s2 (False)

    Display if s4 is a subset of s2 (True)
'''
def create_sets(display=None):
    s2 = []
    s3 = []
    s4 = []
    for num in range(1,21):
        if num % 2 == 0:
            s2.append(num)
        if num % 3 == 0:
            s3.append(num)
        if num % 4 == 0:
            s4.append(num)
    s2 = set(s2)
    s3 = set(s3)
    s4 = set(s4)
    if not display:
        print(s2)
        print(s3)
        print(s4)
    if s3 <= s2:
        print(s2)
        print(s3)
        print(s4)
    if s4 <= s2:
        print(s2)
        print(s3)
        print(s4)

create_sets()

# Part 4
'''
    Create a set with the letters in ‘Python’ and add ‘i’ to the set.

    Create a frozenset with the letters in ‘marathon’.

    Display the union and intersection of the two sets.
'''
def create_Pset(display=None):
    s = []
    for key, letter in enumerate('Python'):
        # print(letter)
        s.append(letter)
    s.append('i')
    s = set(s)
    return s
python_set = create_Pset()
marathon_set = frozenset('marathon')
# print(python_set marathon_set)
print(python_set | marathon_set)
print(marathon_set & python_set)