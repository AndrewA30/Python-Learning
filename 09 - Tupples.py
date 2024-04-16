#contoh tupple
x = (9,4,5)

print(type(x))
# isi dari tupple tidak dapat diubah

#tupple juga dapat langsung di define namanya contoh
(x,y,z) = ((9,3),4,5)
print(x)

#cara melakukan sort di tupple menggunakan dictionary
d = {'a':10,'b':2,'c':5,'e':30,'d':20}
print(d.items()) #ubah jadi tupple
#sort menggunakan for dan fucntion sorted
for k,v in sorted(d.items()):
    print(k,v)
#cara ubah jadi list
listi = list()

for k,v in d.items():
    listi.append((v,k));

print(sorted(listi));
print(max(listi));

#cara lebih singkat (kalau tidak mengerti pake cara diatas saja)
print(sorted( [(v,k) for k,v in d.items()] ))