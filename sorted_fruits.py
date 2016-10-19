# reads in the fruits from the file unsorted_fruits.txt
infile = open("unsorted_fruits.txt", "r")

# writes fruits out in alphabetical order to a file named sorted_fruits.txt.
outfile=open("sorted_fruits.txt","w")

#from infile, scan the lines so you can do things to them
fruit=infile.readlines()

#from the infile, sort the lines alphabetically
fruit.sort()

# We're going to go ahead and take what we've done with fruit
# aka, the "infile", and create a list that takes out those
# blank lines
newFruit = []
for line in fruit:
    if not line.isspace():
        newFruit.append(line)

# This exists solely for error-checking in the IDLE 
print (newFruit)

# Write all the lines to the "outfile" we previously named with the list
# generated to newFruit
outfile.writelines(newFruit)

# Prevent memory leak
infile.close()

# Prevent memoryleak
outfile.close()

# End
