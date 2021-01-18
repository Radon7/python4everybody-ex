"""
Like 9.4 but i want the most 5 frequent
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
# gets the tuple
sort_freq = sorted([(v, k) for k, v in counts.items()], reverse=True)
for v, k in sort_freq[:5]:
    print(k, v)
"""   
big_count = None
big_key = None
for k, v in counts.items():
    if big_count is None or v > big_count:
        big_key, big_count = k, v
print(big_key, big_count)
# alternative to a for loop
big_key = max(counts)
print(big_key, counts[big_key])
"""
