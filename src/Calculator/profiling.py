#!/usr/bin/env python3
# IVS projekt 2 - profiling
# Pavlina Auerova

import matlib
import sys

# arguments handling
if (len(sys.argv) > 1):
    sys.stderr.write("Invalid input - you must enter some data.\n")
    sys.exit(2)

# input processing
try:
    numbers = list(map(int, sys.stdin.read().split()))

    if (numbers == []):
        sys.stderr.write("Invalid input - you must enter some data.\n")
        sys.exit(2)

except (ValueError, KeyboardInterrupt):
    sys.stderr.write("Invalid input data, not a number or keyboard interrupt.\n")
    sys.exit(2)


# Calculating standard deviation
def standardDeviation(numbers):
    count = len(numbers)

    if count < 2:
        sys.stderr.write("Invalid input data, numbers count must be greater than 2.\n")
        sys.exit(2)

    # arithmetical mean and deviation summary
    arMean = 0.0
    devSummary = 0.0

    for num in numbers:
        arMean = matlib.add(arMean, num)
        devSummary = matlib.add(devSummary, matlib.pow(num, 2.0))

    # Average calculating
    arMean = matlib.div(arMean, count)

    # Deviation calculating
    deviation = matlib.nroot(matlib.div(matlib.sub(devSummary, matlib.mul(count, matlib.pow(arMean, 2.0))),
                                        matlib.sub(count, 1.0)), 2.0)
    print(deviation)


try:
    standardDeviation(numbers)
except:
    sys.stderr.write("An unexpected error occurred.\n")
    sys.exit(2)
