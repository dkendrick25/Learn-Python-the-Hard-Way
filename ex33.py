

def while_loop_prac(n, inc):
    i = 0
    numbers = []
    while i < n:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + inc
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

while_loop_prac(10, 2)
