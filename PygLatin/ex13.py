from sys import argv

script, first, second = argv

print "this is script = " , script
print "1st =", first
print "2nd =", second
third = raw_input("3rd = ")
print 'THIRD = %r' % (
	third)