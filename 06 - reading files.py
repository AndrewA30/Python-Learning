fhandle = open("Interview.txt","r")
#cara 1 untuk membaca isi file
# count = 0
# for x in fhandle:
#     x = x.rstrip()
#     count = count + 1
#     print ("Line = ",count,x)
# print ("total line count = ",count)

#cara kedua untuk membaca isi file

# readfile = fhandle.read()
# print(readfile)
# print (len(readfile))
# print(readfile[0:1000])

# cara menampilkan data yang diinginkan saja (cara ini bisa dipake jika linenya dikit saja)
# count = 0
# for x in fhandle:
#     x = x.rstrip() #pake rstrip untuk menghilangkan line tambahan
#     count = count + 1
#     if x.startswith("Normalisasi"):
#         print ("Line = ",count,x)
# print ("total line count = ",count)

# cara lebih cepat
# count = 0
# for x in fhandle:
#     x = x.rstrip() #pake rstrip untuk menghilangkan line tambahan
#     count = count + 1
#     if not "Normalisasi" in x :
#         continue;
#     else : print ("Line = ",count,x)
# print ("total line count = ",count)

# filename = input("Masukkan nama file (beserta extension) = ")
# try:
#     readfile = open(filename,"r");
# except:
#     print("Nama file tidak ditemukan, nama file kamu adalah", filename)
#     quit();


# for x in readfile:
#     x = x.rstrip()
#     print(x)
# readfile.close()