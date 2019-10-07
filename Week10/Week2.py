# this string is telling us the types of people
x = "There are %d types of people." % 10\
# this is a string
binary = "binary"
# and so is this one
doNot = "don't"
# this string tells us what they know
y = "Those who know %s and those who %s." % (binary, doNot)

print(x)
print(y)

print("I said: %r" % x)
print("I also said: '%s' ." % y)

# hilarious + false because the joke was not funny
hillarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print(joke_evaluation % hillarious)

# these two are the two sides of a string
w = "This is the left side of..."
e= "a string with a right side."

print(w + e)


