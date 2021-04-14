#!/usr/bin/env python3
# IVS projekt 2 - profiling
# Pavlina Auerova

import matlib
import sys

if (len(sys.argv) != 1):
    sys.stderr.write("Invalid number of arguments.\n")
    sys.exit(2)

data = []
while True:
    try:
        line = input()
        if line:
            data.append(line.split(" "))
        else:
            break
    except EOFError:
        break
    except:
        sys.stderr.write("An unexpected error occurred.\n")
        sys.exit(2)

data_str = [val for sublist in data for val in sublist]

try:
    numbers = list(map(int, data_str))
except ValueError:
    sys.stderr.write("Invalid input data - not a number.\n")
    sys.exit(2)

# arithmetical mean and deviation summary
def standardDeviation(numbers):

    count = len(numbers)

    if (count == 0):
        sys.stderr.write("Invalid input data, numbers count must be greater than 2.\n")
        sys.exit(2)

    arMean = 0.0
    devSummary = 0.0

    for num in numbers:
        arMean = matlib.add(arMean, num)
        devSummary = matlib.add(devSummary, matlib.pow(num, 2.0))

    arMean = matlib.div(arMean, count)

    deviation = matlib.nroot(matlib.div(matlib.sub(devSummary, matlib.mul(count, matlib.pow(arMean, 2.0))), matlib.sub(count, 1.0)), 2.0)
    print(deviation)

try:
    standardDeviation(numbers)
except:
    sys.stderr.write("An unexpected error occurred.\n")
    sys.exit(2)
