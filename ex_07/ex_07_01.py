fh = open('mbox.txt')

for line in fh:
    up_line = line.rstrip().upper()
    print(up_line)
