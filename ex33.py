i = 0
numbers = []
def loop(i):
    while i < 6:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

loop(i)

print "The numbers: "

for num in numbers:
    print num
