food_prefs = {
    "name": "Chris",
    "city": "Seattle",
    "cake": "chocolate",
    "fruit": "mango",
    "salad": "greek",
    "pasta": "lasagna"
}

'''
    Print the dict by passing it to a string format method, so that you get something like:

       “Chris is from Seattle, and he likes chocolate cake, mango fruit, greek salad, and lasagna pasta.”

    Using a list comprehension, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent. String is fine. The hex() function gives you the hexidecimal representation of a number as a string.

    Do the previous entirely with a dict comprehension. This should be a one-liner.

    Using the dictionary from item (1), make a dictionary using the same keys but with the number of ‘a’s in each value. You can do this either by editing the dict in place, or making a new one. If you edit in place make a copy first!

    Create sets s2, s3, and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.

            Do this with one set comprehension for each set.

            What if you had a lot more than 3? – Don’t Repeat Yourself (DRY).

                    Create a sequence that holds all the divisors you might want. It could be 2,3,4, or could be any other arbitrary divisors.

                    Loop through that sequence to build the sets up – so no repeated code. You will end up with a list of sets – one set for each divisor in your sequence.

                    The idea here is that when you see three (Or more!) lines of code that are almost identical, then you you want to find a way to generalize that code and have it act on a set of inputs, so the actual code is only written once.

            For extra credit, do it all as a one-liner by nesting a set comprehension inside a list comprehension. (OK, maybe this is getting carried away!)

'''