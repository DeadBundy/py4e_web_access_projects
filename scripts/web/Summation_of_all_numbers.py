import re

handle = open("../../data/regex_sum_2284799.txt")
tot = list()
for line in handle:
    line = line.rstrip()
    a = re.findall('[0-9]+',line)
    for num in a:
        change_type = float(num)
        tot.append(change_type)
print("summation:", int(sum(tot)))
