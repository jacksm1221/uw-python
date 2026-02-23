import re
'''
In 'students.txt', you will find a list of names and what 
programming languages they have used in the past. 
This may be similar to a list generated at the beginning of this class.

Write a little script that reads that file and generates a 
list of all the languages that have been used.

What might be the best data structure to use to
 keep track of bunch of values (the languages) without duplication?
The File Format

The first line of the file is:

Name: Nickname, languages

And each line looks something like this:

Jagger, Michael: Mick, shell, python

So a colon after the name, then the nickname, and then one or more languages.

However, like real data files, the file is NOT well-formed. 
Only some lines have nicknames, and other small differences, 
so you will need to write some code to make sure you get it all correct.

How can you tell the difference between a nickname and a language?

Extra challenge: keep track of how many students specified each language.
'''
#
with open("students.txt", "r") as p2_in, open("copy.txt", "w") as p2_out:
    # Pull data
    data = p2_in.read()
    data = data.splitlines()
    # List each unique language used
    language_list = []
    for key, item in enumerate(data):
        colon = item.find(":")
        languages = item[colon+2:]
        for i in languages.split(', '):
            if i in language_list:
                continue
            elif i.islower():
                language_list.append(i)
            else:
                continue
    language_list = set(language_list)
    # print(language_list)
    # List amount each unique language used
    new_langlist = {}
    for j in language_list:
        new_langlist.update({j: 0})
        for each in data:
            colon = each.find(":")
            languages = each[colon+2:]
            # new_langlist[j] += len(re.findall(j, languages))
            new_langlist[j] += languages.count(str(j))
    print(new_langlist)
print(p2_in.closed)
print(p2_out.closed)