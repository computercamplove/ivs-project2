#!/usr/bin/env python3
# IVS projekt 2 - profiling
# Pavlina Auerova

import matlib

# nacte vstup (random cisla) a vrati pole
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

data_str = [val for sublist in data for val in sublist]
numbers = list(map(int, data_str))
#print(numbers)

# arithmetical mean and deviation summary

count = len(numbers)

# TODO osetreni pokud je count < 2

arMean = 0.0
devSummary = 0.0

for num in numbers:
    arMean = matlib.add(arMean, num)
    devSummary = matlib.add(devSummary, matlib.pow(num, 2.0))

arMean = matlib.div(arMean, count)

deviation = matlib.nroot(matlib.div(matlib.sub(devSummary, matlib.mul(count, matlib.pow(arMean, 2.0))), matlib.sub(count, 1.0)), 2.0)

print(deviation)







