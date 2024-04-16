import re

fhandle = open("Interview.txt","r")

for line in fhandle:
    line = line.rstrip() #pake rstrip untuk menghilangkan line tambahan
    if re.search("Normalisasi",line):
        print ("Line = ",line);

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x);

x = "My 2 favourite number are 7 and 8"
y = re.findall('[0-9]+',x)
print(y)

y = re.findall('[a-z]+',x)
print(y)

y = re.findall('[aeiou]+',x)
print(y)
#ambil semua
y = re.findall('M.+',x)
print(y)
#ambil yg cocok saja
y = re.findall('M.+?',x)
print(y)

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)

#extract kata
apos = s.find('@')
bpos = s.find(' ',apos)
print(apos,bpos)
print(s[19:29])

words = s.split()
email = re.findall('[@]\\S+',s)
print(email, email2)