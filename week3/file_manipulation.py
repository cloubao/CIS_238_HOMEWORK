#!/usr/bin/python

# Open the file for writing 
file = open("test.txt","w") 
file.write("Hello world\n") 
file.close()

# Open the file for appending 
file = open("test.txt","a") 
file.write("This is the end\n") 
file.close()

# Open the file for reading and modification 
file = open("test.txt","r+")

# Print file contents 
print "Current contents are:\n" + file.read()

# Go to the end of the file and append 
file.seek(0,2)
print "Starting file length is %d" % file.tell()

file.write("This is the new end!\n")
print "End file length is %d" % file.tell()

# Go back to the beginning of the file for reading 
file.seek(0,0) 
print "\nNew contents are:\n" + file.read()
file.close()