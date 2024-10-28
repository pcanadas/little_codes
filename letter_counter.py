'''
Given a string as input, the program generates a dictionary representing the number of times each letter appears in the string.

Sample Input
hello

Sample Output
H: 1 time
e: 1 time
l: 2 times
o: 1 time
'''
text = input('Please insert a text: ')
dict = {}

key = ()
for letter in text:
    if letter not in key:
        key = key + tuple(letter.split())
for i in key:
    count = 0
    for letter in text:
        if i == letter:
            count += 1
        dict[i] = count
        
for key, value in dict.items():
    if value == 1:
        print(f'{key}: {value} time')
    else:
        print(f'{key}: {value} times')       