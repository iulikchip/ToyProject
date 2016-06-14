from sys import argv 
from os.path import exists 

script, from_file, to_file = argv 

print "Copying from %s to %s " % (from_file, to_file)

#in_file = open(from_file)
    
#   method 1, file.read(name of file)
#in_data = file.read(in_file)

#   method 2, var_name = in_file(type file).read() 
#in_data = in_file.read()

#   method 3, var_name = open(name of file).read()
#   don't close the file. 


in_data = open(from_file).read()

print "The input file is %d bytes long " % len(in_data)

print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()

out_file = open(to_file, 'w').write(in_data)

#   out_file.write(in_data)

print "Done."

#   don't close the file. 
#   in case of method 3 
#out_file.close()
#in_file.close()