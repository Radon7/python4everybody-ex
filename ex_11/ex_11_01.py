import re

name = input("Filename here: ")
if len(name) < 1:
    name = "regex_sum_42.txt"
fh = open(name, "r")
total = 0
for line in fh:
    total += sum([int(num) for num in re.findall("[0-9]+", line.rstrip())])

print(total)
