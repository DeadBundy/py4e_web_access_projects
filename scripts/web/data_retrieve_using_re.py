import re

handle = open("../../data/mbox-short.txt")
for line in handle:
    line.rstrip()
    if re.search("^Jan", line): #returns true or false
        print(line)

#instead of using startswith, we use regular expression ^ symbol which means
#string starting with that character

    #if re.search("^M.*:", line): #meaning print all starting with 'X' and having any other character any number of time or none till colon
        #print(line)

    if re.search("^X-\S+:", line): #gives starting w 'X' followed by -, having any non-whitespace character >=1 till colon
        print(line)