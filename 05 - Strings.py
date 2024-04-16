fruit = 'banana'
let = fruit[0]

print(let)

for i in fruit:
    print(i)
print("Panjang Karakter ",len(fruit))

s = "Andrew Avellino"
print(s[0:5])

#concat in python
s = s + " " +"Kaya"
print(s)

s = s.lower()
print(s)
print(s.upper())

print("Print Posisi karakter ",fruit.find('a'))

print(s.lower().replace('andrew','Cheryl'))

#remove spasi bisa pake strip, lstrip, rstrip
print(s.strip())

#contoh ingin mengambil karakter avellino saja dari tulisan andrew avellino kaya
print(s[s.find(" "):s.find(" kaya",s.find(" "))].strip())
#mengambil tulisan andrew
print(s[0:s.find(" ")])
#mengambil tulisan kaya
#notes [] digunakan untuk menagambil range contoh [0:] -> artinya mengambil dari karakter awal sampai akhir [0:1]-> artinya mengambil karakter 0 sampai 1
print(s[s.find("no ")+3:])