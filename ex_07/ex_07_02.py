# Use the file name mbox-short.txt as the file name
f_name = input("Enter file name: ")
fh = open(f_name)
count = 0
total = 0.0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        conf_str = line[line.find(":") + 1:].strip()
        total += float(conf_str)
print("Average spam confidence:", (total / count))
