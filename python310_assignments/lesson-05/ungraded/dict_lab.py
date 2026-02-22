d = {
    "name": "Chris",
    "city": "Seattle",
    "cake": "chocolate"
}

# Part 1
print(d)
d.pop("cake")
print(d)
d.update({"fruit": "mango"})
print("mango" in d.values())

# Part 2
d2 = {}
for key, value in d.items():
    d2.update({key: value.count("t")})
print(d2)

# Part 3
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
