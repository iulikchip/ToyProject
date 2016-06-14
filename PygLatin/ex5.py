name = 'User Unknown'
age = 28
heightInM = 1.76 # mm
g_ConstInches = 39.370 # Global Constant Coefficient to convert Meters to Inches
heightInInches = heightInM * g_ConstInches
weightInKg = 55 # kg
g_ConstPounds = 2.2
weightInPounds = weightInKg * g_ConstPounds
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about me - %s" % name
print "I am %f m tall. This is %r in Inches"  % ( heightInM , heightInInches)
print "Currently I have %d kilos or %f pounds"  % (weightInKg, weightInPounds)
print "I have %s eyes and %s hair. " % (eyes, hair)
print "If I add %d, %f, and %d I get %f. " % (age , heightInM, weightInKg, age + weightInKg + heightInM)