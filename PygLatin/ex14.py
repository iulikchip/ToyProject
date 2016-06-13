from sys import argv

script, user_name = argv
prompt = 'please, enter a value...\n'

print "Hi %s, this is the %s script. " % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer you have?" 
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.
And you have a %r computer. Nice.
""" % (likes, lives, computer
	)