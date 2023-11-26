# Use open function to read the content of a file!
# f=open('sample.txt','r')
f=open('sample.txt')  #  By default the mode is r.
# data=f.read()
data=f.read(5)  # read first 5 charecters frome the file
print(data)
f.close()