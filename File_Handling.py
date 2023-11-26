# file = open("Intro.txt","w")  # for write mode open file.if file does not exist than create first and then write.

# file.write("Hi, I am karan.\n")
# file.write("I am student of LDCE Ahmedabad.")
# file.close()

# file1 = open("Intro.txt","r")   # Read mode open file.
# print(file1.read())
# file1.close()

file2 = open("Intro.txt", "a")  # appending in file new information.
file2.write("\nLerning python programing")

# we also write, read, and append mode in binnary formate.
# write binnary : wb
# read binnary : rb
# append binnary : ab