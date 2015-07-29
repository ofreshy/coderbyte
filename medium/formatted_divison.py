def FormattedDivision(num1,num2): 
    full , fraction = ("%.4f" % (float(num1) / float(num2))).split('.')
    return ".".join(["{:,}".format(int(full)), fraction])


print FormattedDivision(503394930, 43)
print FormattedDivision(500, 20)
print FormattedDivision(9112, 2)


print "{:,}".format(1000000)