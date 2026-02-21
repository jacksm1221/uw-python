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
