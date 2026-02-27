food_prefs = {
    "name": "Chris",
    "city": "Seattle",
    "cake": "chocolate",
    "fruit": "mango",
    "salad": "greek",
    "pasta": "lasagna"
}

# Print the dict by passing it to a string format method, so that you get something like:
#    “Chris is from Seattle, and he likes chocolate cake, mango fruit, greek salad, and lasagna pasta.”
# print("{} is from {}, and he likes {} cake, {} fruit, {} salad, and {} pasta.".format(*food_prefs.values()))


# Using a list comprehension, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent.
# String is fine. The hex() function gives you the hexidecimal representation of a number as a string.
# Do the previous entirely with a dict comprehension. This should be a one-liner.
hex_comprehension = [{i : hex(i) for i in range(15+1) }]
# print(hex_comprehension)

# Using the dictionary from item (1), make a dictionary using the same keys but with the number of ‘a’s in each value.
# You can do this either by editing the dict in place, or making a new one. If you edit in place make a copy first!
a_comprehension = {i : i.count('a') for i in food_prefs}
# print(a_comprehension)


# Create sets s2, s3, and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
    # Do this with one set comprehension for each set.
s2 = (i for i in range(20+1) if i%2==0)
s3 = (i for i in range(20+1) if i%3==0)
s4 = (i for i in range(20+1) if i%4==0)
# print(*s2, *s3, *s4)

    # What if you had a lot more than 3? – Don’t Repeat Yourself (DRY).
        # Create a sequence that holds all the divisors you might want. It could be 2,3,4, or could be any other arbitrary divisors.
        # Loop through that sequence to build the sets up – so no repeated code. You will end up with a list of sets – one set for each divisor in your sequence.
        # The idea here is that when you see three (Or more!) lines of code that are almost identical, then you you want to find a way to generalize that code and have it act on a set of inputs, so the actual code is only written once.
        # For extra credit, do it all as a one-liner by nesting a set comprehension inside a list comprehension. (OK, maybe this is getting carried away!)
set_comp = (j for i in range(1, 6) for j in range(1, 20+1) if j%i==0)
print(*set_comp)