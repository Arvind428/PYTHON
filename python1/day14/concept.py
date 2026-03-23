for letter in 'geeksforgeeks':
    if letter=='e' or letter=='s':
        continue# returns the statement to begining (i.e it doesnt print the next line)
    print('current letter:',letter)

#Break Statement
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break
#this statement stoops the loop when the condition  is found
print('Current Letter :', letter)

#Pass Statement
for letter in 'geeksforgeeks':
    pass
# in this the pass statement passes the loop until the very last
# where we cant find dtring to pass so the loop stops passing and prints the last letter s 
print('Last Letter :', letter)
