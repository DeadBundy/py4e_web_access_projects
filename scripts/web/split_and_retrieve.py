import re
from tkinter.scrolledtext import example

x = "My fav 2 numbers are 24 and 533: aeiou"
y = re.findall('[0-9]+:', x) #splits and returns a list ONLY ending with colon ':'
print(y)
m = re.findall('[0-9]*',x) #splits each string and whitespace into a character to check
print(m)
q = re.findall('[0-9]+',x) #prints also the one WITH colon
print(q)

vov = re.findall('[aeiou]+', x) #it IS case-sensitive
print(vov)


next_line = "From: Using the : characters"
a = re.findall('^F.+:', next_line) # '+' and '*' use greedy method that means itll go on till it finds last colon ':'
print(a)

b = re.findall('^F.+?:', next_line) # '?' non-greedy gives the shortest
print(b, '\n\n')




count = dict()
another = dict()
file_read = open("../../data/mbox-short.txt")
for line in file_read:
    line = line.rstrip()
    email = re.findall(r'^From (\S+@\S+)',line) #will extract only with ()
    at_after = re.findall('^From .*@([^ ]*)', line) #[^XYZ] means anything but 'X', 'Y', 'Z'
    if email:
        e = email[0]
        count[e] = count.get(e, 0) + 1
    if at_after:
        aaa = at_after[0]
        another[aaa] = another.get(aaa, 0) + 1

print(sorted( ((v,k) for (k,v) in count.items()), reverse=True))
print(len(count))

print(sorted(((v,k) for (k,v) in another.items()), reverse=True))


#to find spam confidence
numlist = list()
with open("../../data/mbox-short.txt") as file_read: #reopen file before using, because after one loop the file pointer sits at the end.
    for line in file_read:
        line = line.rstrip()
        stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line) #returns a list
        if not stuff:
            continue
        num = float(stuff[0])
        numlist.append(num)

print("MAXIMUM:", max(numlist))

test = 'we just received $10.00 for cookies!'
r = re.findall('\$[0-9.]+',test) #[0-9.] means a digit OR a period, \ used to specify '$' as a symbol and not re
print(r)