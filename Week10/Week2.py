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


# More stuff 10-8

print("Mary had a little lamb.")
print("Its fleece was what as %s." % 'snow')
print("And everywhere that Mary went.")
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Makes a statement/sentence
print(end1 + end2 + end3 + end4 + end5 + end6  + end7 + end8 + end9 + end10 + end11 + end12)

# More formating
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))

# Why did I use %r instead of %s
# Used r because its a factor not a string

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"

print()
print()







# What if I didnt like Jan being listed on the line with the rest of the
# Test and away from the other months? How could I fix that?

# More escaping

tabbyDog = "\tI'm tabbed in."
persianDog ="I'm split\non a line."
backslashDog = "I'm \\ a \\ dog"
taskDog = """
Ill make a list:
\t* Dog food
\t* chicken
\t* Dog treats\n\t* bone
"""
print(tabbyDog)
print(persianDog)
print(backslashDog)
print(taskDog)