# What have I learned so far
# Printing
print "test"

# format strings
print "I have %d apples" % 10

# argv - taking inputs from command line
# raw_input() - taking inputs from the user while the script is running

# functions and their return values
def add(a, b):
    print "ADDING two numbers: %d + %d" % (a, b)
    return a + b


# opening, reading, and writing to files
f = open(test.txt, 'w')
print f.read()
f.write("hello")

# variables and using them
f = 10
d = 3

print f + d
