### Level 1
##Q1
#For Loop 0-10
# for number in range(11):
#     print(number)
#     number += 1

#While Loop 0-10
# number = 0
# while number in range(11):
#     print(number)
#     number += 1

##Q2
#For Loop 10-0
# for number in range(11,0):
#     print(number)
#     number -= 1
# else:
#     print(f'The loop ended at {number}.')
# for number in range(10,-1,-1):
#     print(number)
# else:
#     print('The loop stops at', number)

# #While Loop 10-0
# number = 10
# while number > -1 :
#     print(number)
#     number -= 1

##Q3
# count = 1
# while count <= 7:
#     hashTag = '#'
#     print(hashTag * count)
#     count += 1

##Q4
count = 1
while count < 64:
    hashtag = '# '
    count += 1
    if count % len(hashtag) == 0 :
        while count < 8:

        continue
    print(hashtag*count)