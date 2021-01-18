"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of
the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string
a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""
name = input("Filename here: ")
if len(name) < 1:
    name = "mbox.txt"
fh = open(name)
counts = dict()
for line in fh:
    wds = line.rstrip().split()
    if len(wds) >= 6 and wds[0] == 'From':
        key = wds[5].split(":")[0]
        counts[key] = counts.get(key, 0) + 1

for k, v in sorted(counts.items()):
    print(k, v)
