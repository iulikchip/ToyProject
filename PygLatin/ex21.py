def add(a,b):
    print "Adding %d + %d" % (a,b)
    return a + b 

def substract(a,b):
    print "SUBSTRACT %d - %d" % (a,b)
    return a - b 

def multiply(a,b):
    print "MULTIPLYING %d * %d " % (a,b)
    return a * b

def divide(a,b):
    print "DIVIDING %d / %d" % (a,b)
    return a / b

print "TIME FOR MATH WITH FUNCTIONS!"

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d \n Height: %d \n Weight: %d \n IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

answer = add(age, substract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", answer, ". Lol right? "