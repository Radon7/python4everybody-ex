"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
they appear in the file. After the dictionary is produced,
the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""
f_name = input("Filename here: ")
fh = open(f_name)
counts = dict()
for line in fh:
    line = line.rstrip()
    wds = line.split()
    if len(wds) >= 2 and wds[0] == "From":
        key = wds[1]
        counts[key] = counts.get(key, 0) + 1
big_count = None
big_key = None
for k, v in counts.items():
    if big_count is None or v > big_count:
        big_key, big_count = k, v
print(big_key, big_count)
# alternative to a for loop
big_key = max(counts)
print(big_key, counts[big_key])
