#   imports system library 
from sys import argv

#   definition of variables. in this case, $0 is the script itself, $1 is the filename
script, filename = argv

#   create variable txt - type file
txt = open(filename)

#   print the contents of the file right away, using txt.read() function
print ("Contents of the file %r \n" ) % filename
print txt.read()

#   prompt the user to input a new name of file
print "Type the filename again? "
file_again = raw_input ("> ") 

#   create variable txt_again and open the file_again file
txt_again = open(file_again)
print txt_again.read()

