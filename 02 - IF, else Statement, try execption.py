# x = 10;
# if , else if dan else statement pada python
# if x < 10:
#     print("Smaller")
# elif x > 10:
#     print("Bigger")
# else:
#     print("Invalid bodoh coba pake angka lain, anga kamu sekarang adalah ",x)
# print("Finish")

#try and catch statement
umur = input("Input Umur kamu =")
try:
    umur = int(umur)
except:
    umur = -1

if umur > 0:
    print("umur kamu adalah ",umur)
else:
    print("Bukan angka")