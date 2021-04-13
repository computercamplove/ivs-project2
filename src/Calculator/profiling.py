#!/usr/bin/env python3
# IVS projekt 2 - profiling
# Pavlina Auerova

# nacte vstup (random cisla) a vrati pole
def getInput():
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
    # (test print) print(numbers)
    return numbers;

print(getInput())





