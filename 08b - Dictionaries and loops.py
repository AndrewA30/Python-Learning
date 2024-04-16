import os
filehandle = open("Interview.txt","r")

readfile = filehandle.read()

# print(readfile)

pisah = readfile.split()

buku = dict();
for x in pisah:
    buku[x] = buku.get(x,0) + 1


# write data dict ke file txt
# path = "D:\Python Learning"

# file1 = open("08b - insert_dictionaries.txt","w+")

# for x in buku:
#     teks = x + " = " + str(buku[x]) +" \n"
#     # print(teks)
#     file1.writelines(teks)

# file1.close

#cara membuat dict menjadi list
# print(list(buku))
#cara kedua
# print(buku.keys())

#untuk mendapatkan valuenya
# print(buku.values())

#cara menjadi tupple yang akan dipelajari selanjutnya
# print (buku.items())

#cara cepat for untuk print dict (harus dijadikan tupple dulu menggunakan items)
bigword = None
bigcount = None
# for x,y in buku.items():
#     print(x,y)
for x,y in buku.items():
    if bigcount is None or y > bigcount:
        bigword = x
        bigcount = y
print(bigcount, bigword)

filehandle.close





