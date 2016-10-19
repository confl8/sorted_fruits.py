## reads in the fruits from the file unsorted_fruits.txt

infile = open("unsorted_fruits.txt", "r")

## writes fruits out in alphabetical order to a file named sorted_fruits.txt.

outfile=open("sorted_fruits.txt","w")

fruit=infile.readlines()

fruit.sort()

outfile.writelines(fruit)

print (fruit)

infile.close()

outfile.close()
