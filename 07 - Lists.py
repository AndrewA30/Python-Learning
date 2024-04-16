#Lists
friends = ["Andrew","Andre","Andreas"]
print(friends)
print(friends[0])

# for i in range(0,5):
#     print(i)

print(len(friends))

friends = friends + ["Avellino"]

for i in friends:
    print(i)

print(len(friends))

#cara lain menggunakan for
# for i in range(len(friends)):
#     print(friends[i])

#create list from scratch
stuff = list()
stuff.append("Book")
stuff.append("1")

print('Book' in stuff)#hasil nya true (untuk mengecek apakah sesuatu ada dalam list yang dibuat)

#coba input ke list
# lista = list()
# while True:
#     inp = input("Masukkan Angka Untuk Mencari Average = ")
#     if inp =="done":
#         break;
#     value = float(inp)
#     lista.append(value)
# avg = sum(lista)/len(lista)
# print("average = ",avg)

abc = "Woi gila la kau"
splitter = abc.split()
print(splitter)

abc = "woi;gila;la;kau"
splitter = abc.split(';')
print(splitter)